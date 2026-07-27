from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler


class PinzoAPIError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "خطایی رخ داده است."
    default_code = "error"


def pinzo_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    if response is None:
        return None

    if isinstance(response.data, dict) and "detail" in response.data:
        message = response.data["detail"]
        code = getattr(exc, "default_code", "error")
        return Response(
            {"success": False, "error": {"code": code, "message": str(message)}},
            status=response.status_code,
        )

    return Response(
        {
            "success": False,
            "error": {
                "code": "validation_error",
                "message": "خطای اعتبارسنجی",
                "details": response.data,
            },
        },
        status=response.status_code,
    )
