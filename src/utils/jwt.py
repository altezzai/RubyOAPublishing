import jwt
from django.conf import settings as django_settings
import datetime as dt

def generate_jwt_token(user):
    """
    Generate a JWT token for the given user
    """
    payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': dt.datetime.now(dt.timezone.utc) + dt.timedelta(days=1)  # Token expires in 1 day
    }
    return jwt.encode(payload, django_settings.JWT_SECRET_KEY, algorithm='HS256')