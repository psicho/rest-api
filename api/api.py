from rest_framework import generics, viewsets
from .serializers import *
from .models import *

from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response


class TopModelList(generics.ListAPIView):
    queryset = TopModel.objects.all()
    serializer_class = TopModelSerializer
    permission_classes = (DjangoModelPermissions,)


class OneInnerList(generics.ListAPIView):
    queryset = OneInner.objects.all()
    serializer_class = OneInnerSerializer
    permission_classes = (DjangoModelPermissions,)


class TwoInnerList(generics.ListAPIView):
    queryset = TwoInner.objects.all()
    serializer_class = TwoInnerSerializer
    permission_classes = (DjangoModelPermissions,)


class ThreeInnerList(generics.ListAPIView):
    queryset = ThreeInner.objects.all()
    serializer_class = ThreeInnerSerializer
    permission_classes = (DjangoModelPermissions,)


class TopModelMixin(object):
    model = TopModel
    serializer_class = TopModelSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = TopModel.objects.all()

        return queryset


class TopModelList(TopModelMixin, generics.ListCreateAPIView):
    pass


class TopModelDetails(TopModelMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class ModelsMixin(object):
    model = Models
    serializer_class = ModelsSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = Models.objects.all()

        return queryset


class ModelsList(ModelsMixin, generics.ListCreateAPIView):
    pass


class ModelsDetails(ModelsMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
