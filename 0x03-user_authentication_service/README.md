# 0x03. User Authentication Service 🪶

![](assets/meme.png)

> Authentication: making sure you are who you say you are, so your data doesn't end up where it shouldn't.

## Project Overview 🪶

This project involves implementing a user authentication service, covering tasks such as:

- creating user models, 
- adding users to a database, 
- finding users, and 
- updating user information.

## 🔧 Requirements and Dependencies:

- Python 3.7
- SQLAlchemy 1.3.x
- bcrypt

##  📚 Tasks:

### 📝 0. User model
---------------------
**📜 Task requirements:**
Create a SQLAlchemy model named `User` for a database table named `users`. The model should have attributes such as `id`, `email`, `hashed_password`, `session_id`, and `reset_token`.

```python
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
```
**Expected Output:**
```yml
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
```

**🗂️ Files:** 
- **[user.py](user.py)**

**🗒️ Description:** 
The file `user.py` contains the SQLAlchemy model `User` with attributes representing user data such as email and hashed password.

### 📝 1. create user
---------------------
**📜 Task requirements:**
Implement the `DB` class provided with the `add_user` method to add users to the database.

```python
from db import DB

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)
```
**Expected Output:**
```
1
2
```

**🗂️ Files:** 
- **[db.py](db.py)**

**🗒️ Description:** 
The `add_user` method in `DB` class adds users to the database with email and hashed password.

### 📝 2. Find user
---------------------
**📜 Task requirements:**
Implement the `DB.find_user_by` method to find users in the database.

```python
from db import DB

my_db = DB()

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")
```
**Expected Output:**
```
1
1
Not found
Invalid
```

**🗂️ Files:** 
- **[db.py](db.py)**

**🗒️ Description:** 
The `find_user_by` method in `DB` class retrieves a user from the database based on specified attributes.

### 📝 3. Update user
---------------------
**📜 Task requirements:**
Implement the `DB.update_user` method to update user information in the database.

```python
from db import DB

my_db = DB()

email = 'test@test.com'
```

**Repo:**

-   GitHub repository: `alx-backend-user-data`
-   Directory: `0x03-user_authentication_service`

## 🎓 Key Takeaways
 - Understanding of SQLAlchemy ORM for database management.
 - Implementation of user authentication functionalities.
 - Hands-on experience with Flask app development.

## 📫 Contact Me

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BinyamMamo)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:binyammamo01@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/binyammamo)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](#)
[![Website](https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://binyammamo.github.io)

<pre id="banner" class="color-change" style="color: #449999" align="center">


 █████╗ ██╗     ██╗  ██╗    ███████╗██╗    ██╗███████╗
██╔══██╗██║     ╚██╗██╔╝    ██╔════╝██║    ██║██╔════╝
███████║██║      ╚███╔╝     ███████╗██║ █╗ ██║█████╗  
██╔══██║██║      ██╔██╗     ╚════██║██║███╗██║██╔══╝  
██║  ██║███████╗██╔╝ ██╗    ███████║╚███╔███╔╝███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚══╝╚══╝ ╚══════╝
                                                      
</pre>