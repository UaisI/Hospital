from rest_framework import viewsets

from .permissions import RoleBasedPermissionsMixin, HasPermissionsByAuthenticatedUserRole


class HospitalGenericViewSet(
    RoleBasedPermissionsMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [HasPermissionsByAuthenticatedUserRole]