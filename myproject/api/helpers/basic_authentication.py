import base64
from functools import wraps
from ..models import giangvien, sinhvien, account
from rest_framework.response import Response

from django.http import JsonResponse, HttpResponse


def basic_auth_required(view_func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if auth_header:
            try:
                auth_type, credentials = auth_header.split(" ")

                if auth_type.lower() != "basic":
                    return HttpResponse("Unauthorized", status=401)

                decoded = base64.b64decode(credentials).decode("utf-8")
                username, password = decoded.split(":", 1)

            except Exception:
                pass

            try:
                user_account = account.objects.get(username=username)

                if user_account.password == password:
                    return view_func(request, *args, **kwargs)

            except Exception:
                pass

        response = HttpResponse("Unauthorized", status=401)
        response["WWW-Authenticate"] = 'Basic realm="Django"'
        return response

    return wrapper
