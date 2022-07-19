from rest_framework import serializers


class LinkSerializer(serializers.ModelSerializer) :
    class Meta:
        model = links
        fields = "__all__"