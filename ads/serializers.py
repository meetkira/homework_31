from rest_framework import serializers

from ads.models import Ad, Category
from ads.validators import MinLengthValidator
from users.models import User


class AdDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='first_name'
    )
    '''image = serializers.SlugRelatedField(
        read_only=True,
        slug_field='url',
        allow_empty=True,
    )'''

    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    category = serializers.SlugRelatedField(
        required=True,
        queryset=Category.objects.all(),
        slug_field='id'
    )
    author = serializers.SlugRelatedField(
        required=True,
        queryset=User.objects.all(),
        slug_field='id'
    )
    name = serializers.CharField(max_length=100, validators=[MinLengthValidator(10)])

    class Meta:
        model = Ad
        exclude = ['image', 'is_published']


class AdUpdateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='id'
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )
    name = serializers.CharField(max_length=100, validators=[MinLengthValidator(10)])

    class Meta:
        model = Ad
        fields = ["name", "price", "description", "is_published", "author", "category"]


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class CatCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    slug = serializers.CharField(max_length=10, validators=[MinLengthValidator(5)])

    class Meta:
        model = Category
        fields = "__all__"


class CatDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id']
