from typing import TYPE_CHECKING

from django.http import HttpRequest
from ninja_extra.permissions.base import BasePermission, SAFE_METHODS
if TYPE_CHECKING:
    from ninja_extra.controllers.base import APIController


__all__ = [
    'AllowAny',
    'IsAuthenticated',
    'IsAdminUser',
    'IsAuthenticatedOrReadOnly'
]


class AllowAny(BasePermission):
    """
    Allow any access.
    This isn't strictly required, since you could use an empty
    permission_classes list, but it's useful because it makes the intention
    more explicit.
    """

    def has_permission(self, request: HttpRequest, controller: "APIController"):
        return True


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request: HttpRequest, controller: "APIController"):
        return bool(request.user and request.user.is_authenticated)


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request: HttpRequest, controller: "APIController"):
        return bool(request.user and request.user.is_staff)


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request: HttpRequest, controller: "APIController"):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
