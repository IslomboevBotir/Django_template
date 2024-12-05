from rest_framework import serializers
from .models import Documents


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'

    @staticmethod
    def validate_pdf_file(file):
        if not file.name.endswith('.pdf'):
            raise serializers.ValidationError("Only PDF files can be uploaded.")
        return file
