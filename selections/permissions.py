from django.http import Http404
from rest_framework.permissions import BasePermission

from selections.models import Selection

class CreateSelectionPermission(BasePermission):
    message = "You can create selection only for yourself"

    def has_permission(self, request, view):
        if request.data["owner"] != request.user.id:
            return False

        return True

class UpdateSelectionPermission(BasePermission):
    message = "You can't update or delete not yours selections"

    def has_permission(self, request, view):
        try:
            selection = Selection.objects.get(id=view.kwargs["pk"])
        except Selection.DoesNotExist:
            raise Http404

        if selection.owner.id != request.user.id:
            return False

        return True
