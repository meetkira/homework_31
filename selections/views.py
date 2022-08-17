from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from selections.models import Selection
from selections.permissions import UpdateSelectionPermission, CreateSelectionPermission
from selections.serializers import SelectionSerializer, SelectionCreateSerializer, SelectionUpdateSerializer, \
    SelectionDestroySerializer


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated, CreateSelectionPermission]


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, UpdateSelectionPermission]


class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDestroySerializer
    permission_classes = [IsAuthenticated, UpdateSelectionPermission]
