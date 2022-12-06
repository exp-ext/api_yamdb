from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnLy(BasePermission):
    message = 'Изменение чужого контента запрещено!'
    
    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user 