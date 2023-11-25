from rest_framework import serializers

from course.models import Subscription

PERMITTED_HOSTING = 'https://www.youtube.com'


def youtube_validator(value):
    if value not in PERMITTED_HOSTING:
        raise serializers.ValidationError('Ссылки на сторонние ресурсы, кроме youtube запрещены.')


# def validate_unique(value):
#     existing_value = Subscription.objects.get()
