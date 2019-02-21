from rest_framework import serializers
from api.models import *


class ThreeInnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeInner
        fields = ('id', 'name',)


class TwoInnerSerializer(serializers.ModelSerializer):
    children = ThreeInnerSerializer(many=True)
    # children = serializers.CharField(source='get_children', read_only=True)

    class Meta:
        model = TwoInner
        fields = ('id', 'name', 'children')


class OneInnerSerializer(serializers.ModelSerializer):
    children = TwoInnerSerializer(many=True, )
    # children = serializers.CharField(source='get_children', read_only=True)

    class Meta:
        model = OneInner
        fields = ('id', 'name', 'children')


class TopModelSerializer(serializers.ModelSerializer):
    # children = serializers.CharField(source='get_children', read_only=True)
    children = OneInnerSerializer(many=True)

    class Meta:
        model = TopModel
        fields = ('id', 'name', 'children')


class ModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TopModel
        fields = ('id', 'name', 'children')
