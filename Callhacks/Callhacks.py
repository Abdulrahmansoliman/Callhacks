import reflex as rx
from typing import Optional

from sqlmodel import Field

from reflex import Model, session, DBConfig

# Configure DB

# Define User model
class User(rx.Model, table=True):
    username: str = Field() 
    email: str = Field()
    password: str = Field()





# Insert new user
with rx.session() as session:
    session.add(
        User(username="test", email="admin@pynecone.io", password="admin"))
    session.commit()

# Retrieve users
users = User.select()
for user in users:
    print(user.username, user.email)

# API route


# @app.api.route("/users")
# async def get_all_users():
#     users = User.select()
#     user_data = [dict(username=u.username, email=u.email) for u in users]
#     return user_data

# Create and compile app
app = rx.App()
app.compile()
