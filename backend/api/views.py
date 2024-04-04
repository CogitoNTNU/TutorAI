from django.http import HttpResponse
from django.db import DatabaseError
from django.core.cache import cache
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, serializers
from rest_framework.response import Response

@swagger_auto_schema(
    method="get",
    operation_description="Health check endpoint",
    responses={200: "OK"},
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def health_check(request) -> Response:
    try:
        # Check cache
        cache.set('health_check', 'ok', timeout=30)
        if cache.get('health_check') != 'ok':
            raise ValueError("Cache not working")

        return Response("OK", content_type="text/plain")
    except (DatabaseError, ValueError) as e:
        return Response(str(e), status=500, content_type="text/plain")