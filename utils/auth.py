from models.user_model import get_user_by_username

def authenticate_user(username, password, role):
    user = get_user_by_username(username)

    if user and user['role'] == role and user['password'] == password:
        return user
    return None

