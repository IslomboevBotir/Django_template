# Blog API

## Запуск проекта
1. Клонируйте репозиторий.
2. Создайте `.env` в корне проекта, используя `.env.example` для примера, и убедитесь, что `DB_HOST` и `DB_PORT` не изменены:
    ```env
    DB_HOST=db
    DB_PORT=5432
    ```
3. Запустите приложение с помощью Docker Compose:
    ```bash
    docker-compose up --build
    ```

## Предустановленные пользователи

В системе создано три тестовых пользователя с различными ролями:

1. **Сотрудник (employee)**:
   - **Логин**: `user1`
   - **Пароль**: `user1user1`
   - **Роль**: Сотрудник может загружать документы и может просмотреть список своих отправленных документов и их статус (на
рассмотрении, принято, отклонено).

2. **Ассистент (assistant)**:
   - **Логин**: `user3`
   - **Пароль**: `user3user3`
   - **Роль**: Ассистент может просматривать только те документы которые были назначены ему начальником, может принять или отклонить документ.

3. **Менеджер (manager)**:
   - **Логин**: `user2`
   - **Пароль**: `user2user2`
   - **Роль**: Менеджер может просматривать все документы, обновлять их статус и назначать документы ассистентам.

# Все запросы рекомендуется отправлять в Postman(так удобнее)!!!


## Эндпоинты
### 1. Авторизация:

#### Получение токена:
**POST /api/auth/token**

**Тело запроса**:
```json
{
  "username": "имя_пользователя",
  "password": "пароль"
}
```
**Пример ответа**:
```json
{
  "access": "access_token",
  "refresh": "refresh_token"
}
```
Нужно при отправке запроса отправлять в Bearer access_token

### 2. Обновление токена:
**POST /api/auth/token-refresh**
**Тело запроса**:
```json
{
  "refresh": "refresh_token"
}
```
**Пример ответа**:
```json
{
  "access": "new_access_token"
}
```

### 3. Проверка токена:
**POST /api/auth/token-verify**
**Тело запроса**:
```json
{
  "token": "access_token"
}
```
**Пример ответа**:
```json
{
  "message": "Token is valid"
}
```
**Пример ответа при ошибке**:
```json
{
  "detail": "Token is invalid or expired",
  "code": "token_not_valid"
}
```

### 4. Создание документа сотрудником
**POST /api/documents/upload**
**Тело запроса**:
```json
{
  "title": "example",
   "mfo": "example MFO",
   "pdf_file": "any pdf file",
   "document_type": "payment OR instruction",
   "message": "Example message",
   "created_by": "This is FK into ofb_core_customuser table"
}
```
**Пример ответа**:
```json
{
    "id": 1,
    "title": "example",
    "pdf_file": "any pdf file",
    "mfo": "example MFO",
    "document_type": "payment OR instruction",
    "message": "Example message",
    "status": "pending",
    "created_at": "2024-12-05T19:28:43.479168Z",
    "created_by": 1,
    "assigned_to": null
}
```

### 5. Назначение документа начальником
**PATCH /api/documents/assign/<int:pk>**
**Тело запроса**:
```json
{
   "assigned_to_id": 3
}
```
**Пример ответа**:
```json
{
  "message":"The document has been assigned to an assistant"
}
```
**Пример ответа при ошибке**:
```json
{
   "error": "Access denied"
}
```
### 6. Назначение статуса принятия или отклонения начальником или помошником начальника
**PATCH /api/documents/status/<int:pk>**
**Тело запроса**:
{
  "message":"approved | rejected"
}
**Пример ответа**:
```json
{
   "message":"Document status updated to 'rejected'| 'approved'"
}
```
**Пример ответа при ошибке**:
```json
{
   "error": "Access denied"
}
```
### 7. Просмотр отправленных документов сотрудником, просмотр отпрлавенных документов сотрудников начальнику и детали каждого.
###    Просмотр документов, назначенных начальником ассистенту и просмотр деталей 
**GET /api/documents/**
**Пример ответа**:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Test Document",
            "pdf_file": "http://localhost:8000/documents/Botir_islomboev_WyCmwoC.pdf",
            "mfo": "123456",
            "document_type": "payment",
            "message": "This is a test document.",
            "status": "rejected",
            "created_at": "2024-12-05T20:07:24.243695Z",
            "created_by": 1,
            "assigned_to": 3
        }
    ]
}
```
**GET /api/documents/<int:pk>**
**Пример ответа**:
```json
{
    "id": 1,
    "title": "Test Document",
    "pdf_file": "/documents/Botir_islomboev_WyCmwoC.pdf",
    "mfo": "123456",
    "document_type": "payment",
    "message": "This is a test document.",
    "status": "rejected",
    "created_at": "2024-12-05T20:07:24.243695Z",
    "created_by": 1,
    "assigned_to": 3
}
```
### 8. Регистрация пользователя
**POST api/register**
**Тело запроса**:
```json
{
    "username": "new_user",
    "email": "new_user@example.com",
    "password": "secure_password",
    "role": "employee"
}
```
**Пример ответа**:
```json
{
    "id": 4,
    "username": "new_user",
    "email": "new_user@example.com",
    "role": "employee"
}
```