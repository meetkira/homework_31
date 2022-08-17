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


'''@method_decorator(csrf_exempt, name="dispatch")
class AdListView(ListView):
    model = Ad
    queryset = Ad.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        cats = request.GET.getlist("cats", [])
        text = request.GET.get("text", None)
        location = request.GET.get("location", None)
        price_from = request.GET.get("price_from", None)
        price_to = request.GET.get("price_to", None)

        if cats:
            self.object_list = self.object_list.filter(category_id__in=cats)
        if text:
            self.object_list = self.object_list.filter(name__icontains=text)
        if location:
            self.object_list = self.object_list.filter(author__locations__name__icontains=location)
        if price_from:
            self.object_list = self.object_list.filter(price__gte=price_from)
        if price_to:
            self.object_list = self.object_list.filter(price__lte=price_to)

        self.object_list = self.object_list.order_by("price")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "image": ad.image.url if ad.image else None,
                "author": ad.author.first_name,
                "category": ad.category.name,
            })

        response = {
            "items": ads,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }

        return JsonResponse(response, safe=False)'''
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
