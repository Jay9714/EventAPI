# EventAPI run using postman
<!-- For setup pls follow below instruction-->
- Python version: 3.12.9
- Install requirements.txt
- All API are added in json format you need to import in postman. File name: EventAPI.postman_collection.json

<!-- For User Registration -->
API 1:- register
<!-- For register New user use below API -->
URL: http://127.0.0.1:8000/api/register/
METHOD: POST

<!-- for postdata follow below step -->
step 1: Select body tab
step 2: Select raw redio button
step 3: Add JSON data

Example of JSON data:
<!-- for creating a user with admin role -->
{
    "username": "techinitiator@admin.com",
    "password": "Admin@9714",
    "user_role": "Admin"
}

OR
<!-- for creating a user with user role -->
{
    "username": "techinitiator@user.com",
    "password": "User@9714",
    "user_role": "User"
}


<!-- To gennerate jwt token use below API -->
API 1:- get_JWT_token
URL: http://127.0.0.1:8000/api/token/
Method: POST

<!-- for postdata follow below step -->
step 1: Select body tab
step 2: Select raw redio button
step 3: Add JSON data
Example of JSON data:
{
    "username": <USERNAME>,
    "password": <PASSWORD>
}


<!-- To gennerate new access token using refresh token use below API -->
API 2:- refresh_JWT_token
URL: http://127.0.0.1:8000/api/token/refresh/
Method: POST
<!-- for postdata follow below step -->
step 1: Select body tab
step 2: Select raw redio button
step 3: Add JSON data
Example of JSON data:
{
    "refresh": <JWT REFRESH TOKEN>
}


<!-- For Event Management -->
API 1:- Create event

<!-- For creating a new event below API -->
URL: http://127.0.0.1:8000/api/events/
METHOD: POST

<!-- Add this in header section for JWT authentication-->
1.  key: Content-Type,
    value: multipart/form-data
2.  key: Authorization,
    value: Bearer <JWT ACCESS TOKEN>

<!-- for postdata follow below step -->
step 1: Select body tab
step 2: Select raw redio button
step 3: Add JSON data
Example of JSON data:
<!-- for creating a user with admin role -->
{
    "name": "KISAN Agri Show",
    "date": "16-02-2025",
    "total_tickets": 10   
}

API 2:- Get events
<!-- For getting all the events -->
URL: http://127.0.0.1:8000/api/events/
METHOD: GET

<!-- Add this in header section for JWT authentication-->
1.  key: Content-Type,
    value: multipart/form-data
2.  key: Authorization,
    value: Bearer <JWT ACCESS TOKEN>


API 3:- get ticket
<!-- For Ticket Purchase -->
URL: http://127.0.0.1:8000/api/events/1/purchase/
METHOD: POST

<!-- Add this in header section for JWT authentication-->
1.  key: Content-Type,
    value: multipart/form-data
2.  key: Authorization,
    value: Bearer <JWT ACCESS TOKEN>

<!-- for postdata follow below step -->
step 1: Select body tab
step 2: Select raw redio button
step 3: Add JSON data
Example of JSON data:
<!-- for creating a user with admin role -->
{
    "quantity": 2
}