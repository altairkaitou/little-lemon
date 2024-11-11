Project: Little Lemon API
=========================

Description:
------------
This project is a RESTful API built using Django Rest Framework (DRF). Below are the available API endpoints for testing. Please use tools like Postman, Insomnia, or `curl` to test the endpoints.

Authentication:
---------------
Before accessing protected endpoints, obtain a token using one of the following endpoints:

1. Obtain a token using Django's built-in token authentication:
   - POST: /restaurant/api-token-auth/
     - Body (JSON):
       {
         "username": "your_username",
         "password": "your_password"
       }

2. Obtain a token using Djoser:
   - POST: /auth/token/login/
     - Body (JSON):
       {
         "username": "your_username",
         "password": "your_password"
       }

Bookings API:
-------------
1. Get all bookings (Requires authentication)
   - GET: /restaurant/booking/tables/

2. Create a new booking (Requires authentication)
   - POST: /restaurant/booking/tables/

Menu API:
---------
1. Get all menu items
   - GET: /restaurant/menu/

2. Get a single menu item by ID
   - GET: /restaurant/menu/<id>/

3. Add a new menu item (Requires authentication)
   - POST: /restaurant/menu/
   - Body (JSON):
     {
       "title": "Pasta Primavera",
       "price": 15.99,
       "inventory": 25
     }

User Registration:
------------------
1. Register a new user
   - POST: /auth/users/
   - Body (JSON):
     {
       "username": "new_user",
       "email": "user@example.com",
       "password": "strongpassword123"
     }

Notes:
------
- Make sure to include the `Authorization` header with the token for protected endpoints:
  - Header:
    Authorization: Token your_generated_token

- For date fields, use the format `YYYY-MM-DD`.
- For time fields, use the format `HH:MM` in 24-hour format.

Thank you for testing the Little Lemon API! If you encounter any issues, please let me know.
