from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Category
from ads.permissions import UpdateAdPermission, CreateAdPermission
from ads.serializers import AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, AdDestroySerializer, \
    CatSerializer, CatCreateSerializer, CatDestroySerializer
from homework_31 import settings


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    permission_classes = [IsAuthenticated, CreateAdPermission]


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, UpdateAdPermission]


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ["image"]

    def patch(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
            "author": self.object.author.first_name,
            "category": self.object.category.name,
        })


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
    permission_classes = [IsAuthenticated, UpdateAdPermission]


class CatListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class CatCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatCreateSerializer


class CatDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class CatUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class CatDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CatDestroySerializer
