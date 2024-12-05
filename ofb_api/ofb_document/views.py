from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from ofb_document.serializer import DocumentsSerializer
from ofb_document.models import Documents
from ofb_core.pagination import CustomPagination


class DocumentsViews(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if user.role == "employee":
            return Documents.objects.filter(created_by=user)
        elif user.role == "manager":
            return Documents.objects.all()
        elif user.role == "assistant":
            return Documents.objects.filter(assigned_to=user)
        return Documents.objects.none()


class DocumentUploadViews(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        if request.user.role != "employee":
            return Response({"error": "Only employees can upload documents"}, status=403)

        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DocumentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            document = Documents.objects.get(pk=pk)

            if request.user.role == "employee" and document.created_by != request.user:
                return Response({"error": "Access denied"}, status=403)

            if request.user.role == "assistant" and document.assigned_to != request.user:
                return Response({"error": "Access denied"}, status=403)

            serializer = DocumentsSerializer(document)
            return Response(serializer.data)
        except Documents.DoesNotExist:
            return Response({"error": "Document not found"}, status=404)


class DocumentStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            document = Documents.objects.get(pk=pk)

            if request.user.role not in ["manager", "assistant"]:
                return Response({"error": "Access denied"}, status=403)

            status = request.data.get("status")
            if status not in ["approved", "rejected"]:
                return Response({"error": "Incorrect status"}, status=400)

            document.status = status
            document.save()
            return Response({"message": f"Document status updated to '{status}'"}, status=200)

        except Documents.DoesNotExist:
            return Response({"error": "Document not found"}, status=404)


class AssignDocumentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            document = Documents.objects.get(pk=pk)

            if request.user.role != "manager":
                return Response({"error": "Access denied"}, status=403)

            assistant_id = request.data.get("assigned_to")
            document.assigned_to_id = assistant_id
            document.save()
            return Response({"message": "The document has been assigned to an assistant"}, status=200)

        except Documents.DoesNotExist:
            return Response({"error": "Document not found"}, status=404)
