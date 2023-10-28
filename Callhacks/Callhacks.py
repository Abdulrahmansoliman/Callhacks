import reflex as rx
from Models.Users import User
import initial

# Define a route to get all users
from reflex import DBConfig


config = rx.Config(
    app_name="Classifier",
    db_url="sqlite:///reflex.db",
    db_config=rx.DBConfig(engine="postgresql+psycopg2", username="Classifier",
                          password="12345", host="localhost", port=5432, database="reflex"),
)

DBConfig.sqlite(database="reflex.db")
DBConfig.postgresql(username="Classifier", password="12345",
                    host="localhost", port=5432, database="reflex")
DBConfig.postgresql_psycopg2(username="Classifier",
                             password="12345", host="localhost", port=5432, database="reflex")


async def get_all_users():
    # Use the User model to query the database and retrieve all users
    users = User.select()

    # Convert the user data to a list of dictionaries
    user_data = [{'username': user.username, 'email': user.email}
                 for user in users]

    return user_data


# Create the app and compile it.
app = rx.App(style=rx.styles.base_style)
app.api.add_api_route("/users", get_all_users)

app.compile()
