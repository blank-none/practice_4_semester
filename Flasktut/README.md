# Encryption Service

---

Этот сервис предоставляет API для шифрования и дешифрования текста методами Цезаря и Виженера.

---

#### Установка и запуск:

1. **Установка зависимостей:**

   ```bash
   pip install flask
   ```

2. **Запуск сервера:**
   ```bash
   python app.py
   ```
   По умолчанию сервер запускается на http://localhost:5000/.

#### API Endpoint's

1. **Добавить пользователя**

   - URL: /users
   - Метод: POST
   - Тело запроса:
     ```json
     {
       "login": "username",
       "secret": "password"
     }
     ```

2. **Получить список пользователей**

   - URL: /users
   - Метод: GET
   - Ответ:
     ```json
     [{ "login": "username1" }, { "login": "username2" }]
     ```

3. **Получить список методов шифрования**

   - URL: /methods
   - Метод: GET
   - Ответ:
     ```json
     [
       {
         "id": "1",
         "caption": "Caesar",
         "json_params": { "shift": "int" },
         "description": "Шифр Цезаря"
       },
       {
         "id": "2",
         "caption": "Vigenere",
         "json_params": { "key": "str" },
         "description": "Шифр Вижинера"
       }
     ]
     ```

4. **Зашифровать/расшифровать данные**

   - URL: /encrypt
   - Метод: POST
   - Тело запроса для шифрования:
     ```json
     {
       "user_id": "username",
       "method_id": "1", // Идентификатор метода (1 для Caesar, 2 для Vigenere)
       "data_in": "plaintext",
       "action": "encrypt",
       "shift": 3 // Параметры шифрования (для Caesar)
     }
     ```
   - Тело запроса для расшифрования:
     ```json
     {
       "user_id": "username",
       "method_id": "2", // Идентификатор метода (1 для Caesar, 2 для Vigenere)
       "data_in": "ciphertext",
       "action": "decrypt",
       "key": "KEY" // Параметры шифрования (для Vigenere)
     }
     ```
   - Ответ: Зашифрованный/расшифрованный текст.

5. **Получить данные по сессиям шифрования**

   - URL: /sessions
   - Метод: GET
   - Ответ:
     Список всех созданных сессий в виде HTML страницы.

6. **Получить подробную информацию о сеансе шифрования**

   - URL: /sessions/{session_id}
   - Метод: GET
   - Ответ:
     Подробная информация о сеансе шифрования в виде HTML страницы.

7. **Удалить сеанс шифрования**
   - URL: /sessions/{session_id}
   - Метод: DELETE
   - Параметры запроса:
     secret: секрет пользователя
   - Ответ: Сообщение об успешном удалении сеанса.

#### Примеры использования:

1. Пример запроса для шифрования методом Цезаря
   - URL: http://localhost:5000/encrypt
   - Метод: POST
   - Тело запроса:
     ```json
     {
       "user_id": "user1",
       "method_id": "1",
       "data_in": "Hello",
       "action": "encrypt",
       "shift": 3
     }
     ```
   - Ответ:
     ```
     "Khoor"
     ```
2. Пример запроса для расшифрования методом Виженера
   - URL: http://localhost:5000/encrypt
   - Метод: POST
   - Тело запроса:
     ```json
     {
       "user_id": "user2",
       "method_id": "2",
       "data_in": "Khoor",
       "action": "decrypt",
       "key": "KEY"
     }
     ```
   - Ответ:
     ```json
     "Hello"
     ```

#### Удаление сеанса шифрования через форму

1. Откройте страницу с деталями сеанса.
2. Введите секрет пользователя и подтвердите удаление сеанса.
