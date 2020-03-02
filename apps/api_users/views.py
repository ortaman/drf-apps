
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from .models import User
from .permissions import UserPermissions
from .serializers import UserSerializer


class UserCreateList(CreateModelMixin, ListModelMixin, GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermissions,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermissions, )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #    return self.destroy(request, *args, **kwargs)
