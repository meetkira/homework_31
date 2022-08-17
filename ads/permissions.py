from django.http import Http404
from rest_framework.permissions import BasePermission

from ads.models import Ad
from users.models import User


class CreateAdPermission(BasePermission):
    message = "You can create ad only for yourself"

    def has_permission(self, request, view):
        if request.data["author"] != request.user.id:
            return False

        return True


class UpdateAdPermission(BasePermission):
    message = "You can't update or delete not yours ads"

    def has_permission(self, request, view):
        try:
            ad = Ad.objects.get(id=view.kwargs["pk"])
        except Ad.DoesNotExist:
            raise Http404

        if ad.author_id == request.user.id:
            return True

        if request.user.role in [User.ADMIN, User.MODERATOR]:
            return True

        return False
