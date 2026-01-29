from rest_framework import serializers
from .models import Page, Container, Row, Column, Component


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'title', 'content_type', 'content', 'image', 'url', 'order']


class ColumnSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True, read_only=True)

    class Meta:
        model = Column
        fields = ['id', 'title', 'width', 'order', 'components']


class RowSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, read_only=True)

    class Meta:
        model = Row
        fields = ['id', 'title', 'order', 'columns']


class ContainerSerializer(serializers.ModelSerializer):
    rows = RowSerializer(many=True, read_only=True)

    class Meta:
        model = Container
        fields = ['id', 'title', 'order', 'rows']


class PageSerializer(serializers.ModelSerializer):
    containers = ContainerSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'content', 'is_published', 'containers']
