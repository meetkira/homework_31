from rest_framework import serializers


class MinLengthValidator:
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) <= self.min_length:
            raise serializers.ValidationError(f"Minimal length {self.min_length}")
