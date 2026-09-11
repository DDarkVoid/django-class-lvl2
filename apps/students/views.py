"""Views for students app."""

from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.students.models import Group, Student, TokenUsage
from apps.students.serializers import GroupSerializer, StudentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """CRUD for Group model."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """CRUD for Student model."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TokenUsageView(APIView):
    """Return request counter for the current token."""

    permission_classes = (IsAuthenticated, )

    def get(self, http_request: Request) -> Response:
        """Return request count for current token."""
        token = http_request.auth
        if not isinstance(token, Token):
            return Response({'request_count': 0})

        usage = TokenUsage.objects.filter(token=token).first()
        if usage is None:
            return Response({'request_count': 0})

        return Response({'request_count': usage.request_count})
