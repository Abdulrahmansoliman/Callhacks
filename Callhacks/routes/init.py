from Callhacks.Models.Users import User

# Define a route to get all users


async def get_all_users():
    # Use the User model to query the database and retrieve all users
    users = User.select()

    # Convert the user data to a list of dictionaries
    user_data = [{'username': user.username, 'email': user.email}
                 for user in users]

    return user_data
