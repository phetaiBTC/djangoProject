from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny
from ..permissions import UserPermissions


class BaseModelViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated, UserPermissions]
    permission_classes = [AllowAny]
