<h1 align=center>Basic login jwt flask API</h1>
<p align=center>
A basic JWT(JSON Web Tokens) based login aunthentication and user handler API system.
The web API is build using Flask and deployed on Heroku with PostgreSQL database.
</p>

# 🔥 Features
* Create Users 
* Multiple roles compatibility like User, Staff, Admin
* Login Authentication using JWT
* Email verification using JWT

# 📑 Endpoints
* ``/api/v1/login [POST]`` : Login using Basic Auth
* ``/api/v1/refresh [POST]`` : Create Refresh Tokens when expired *(Access Tokens expire after 30 minutes)*
* ``/api/v1/confirm [GET]`` : Verifies the email confirmation link *(email verification token is supplied as a parameter in the URL)*
* ``/api/v1/users/ [POST]`` : Creating Users
* ``/api/v1/users/me [POST]`` : View personal information
* ``/api/v1/users/me [PUT]`` : Update personal information
* ``/api/v1/users/me/change_password [PUT]`` : Updates user password
* ``/api/v1/users/me/verify_email [POST]`` : Creates a verify email request and sends email with confirmation link
* ``/api/v1/users/ [GET]`` (admin only) : View all users' information
* ``/api/v1/users/<public_id> [GET]`` (admin only) : View a single user's information
* ``/api/v1/users/<public_id> [PUT]`` (admin only) : Promotes a user to Staff or Admin *(role=Staff or role=Admin is supplied as a parameter in the URL)*
* ``/api/v1/users/<public_id> [DELETE]`` (admin only) : Deletes a user from database


# 🔨 Installation
1. Clone this repo using ``git clone https://github.com/sarvagya14503/basic-login-jwt-flask-API.git``
2. Install the prerequisites using ``pip install -r requirements.txt``
3. Install the [PostgreSQL](https://www.postgresql.org/download/) in your system.
4. Prepare the PostgreSQL database by 
```bash 
python
>>from /src/models import db
>>db.create_all()
>>exit()
```

# 🏷️ Notes
* Checks for 'x-access-token' and 'x-refresh-token' in request headers
* Email verification is set up for Gmail server only, and for that you need to allow your gmail account to be accessed by "Less Secure Apps" by enabling that option through [this link](https://myaccount.google.com/lesssecureapps).
* Error codes are mentioned at places in the source code to handle response in the frontend
