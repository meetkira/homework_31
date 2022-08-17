from rest_framework import serializers

from ads.models import Ad
from ads.serializers import AdDetailSerializer
from selections.models import Selection
from users.models import User


class SelectionSerializer(serializers.ModelSerializer):
    items = AdDetailSerializer(many=True)
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    items = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Ad.objects.all(),
        slug_field='id',
    )
    owner = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = Selection
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._items = self.initial_data.pop('items')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        selection = Selection.objects.create(**validated_data)
        for item in self._items:
            try:
                ad = Ad.objects.get(id=item)
            except Exception:
                continue
            selection.items.add(ad)
        selection.save()
        return selection


class SelectionUpdateSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Ad.objects.all(),
        slug_field='id',
    )
    owner = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        required=False,
        slug_field='id',
    )

    class Meta:
        model = Selection
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        if self.initial_data.get('items'):
            self._items = self.initial_data.pop('items')
        else:
            self._items = None
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        selection = super().save()
        if self._items:
            for item in self._items:
                try:
                    ad = Ad.objects.get(id=item)
                except Exception:
                    continue
                selection.items.add(ad)
            selection.save()
        return selection


class SelectionDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id']
