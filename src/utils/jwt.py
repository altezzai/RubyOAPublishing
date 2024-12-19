# This file was added by Aswin-Koroth on Thu Sep 19 2024.
# - Added for jwt support.

import jwt
from django.conf import settings as django_settings
import datetime as dt


def generate_jwt_token(user):
    """
    Generate a JWT token for the given user
    """

    payload = {
        "user_id": user.id,
        "username": user.osp_username,
        "role": user.osp_role,
        "profile_image": user.profile_image.url if user.profile_image else "",
        "is_citizen_active": user.is_citizen_active,
        "is_knowledge_active": user.is_knowledge_active,
        "exp": dt.datetime.now(dt.timezone.utc)
        + dt.timedelta(days=1),  # Token expires in 1 day
    }
    return jwt.encode(payload, django_settings.JWT_SECRET_KEY, algorithm="HS256")


def decode_jwt_token(request):
    """
    Decode a JWT token
    """
    token = request.headers.get("Authorization", "").split(" ")[1]
    return jwt.decode(token, django_settings.JWT_SECRET_KEY, algorithms=["HS256"])
