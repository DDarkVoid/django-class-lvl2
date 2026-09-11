"""Middleware that counts API requests per token."""

from typing import Callable, Final

from django.http import HttpRequest, HttpResponse
from rest_framework.authtoken.models import Token

from apps.students.models import TokenUsage

TOKEN_PREFIX: Final[str] = 'Token '


class TokenUsageMiddleware(object):
    """Increment request counter for each authenticated request."""

    def __init__(
        self,
        get_response: Callable[[HttpRequest], HttpResponse],
    ) -> None:
        """Store next middleware handler."""
        self._get_response = get_response

    def __call__(self, http_request: HttpRequest) -> HttpResponse:
        """Process request, then return response."""
        self._increment_counter(http_request)
        return self._get_response(http_request)

    def _increment_counter(self, http_request: HttpRequest) -> None:
        """Increment counter for the token in Authorization header."""
        auth_header = http_request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith(TOKEN_PREFIX):
            return

        token_key = auth_header[len(TOKEN_PREFIX):].strip()
        token = Token.objects.filter(key=token_key).first()
        if token is None:
            return

        usage = TokenUsage.objects.filter(token=token).first()
        if usage is None:
            usage = TokenUsage.objects.create(token=token, request_count=0)

        usage.request_count += 1
        usage.save(update_fields=('request_count', ))
