from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from .models import Slider, Page, Container, Row, Column, Component


class ComponentInline(NestedStackedInline):
    model = Component
    extra = 1
    sortable_field_name = "order"


class ColumnInline(NestedTabularInline):
    model = Column
    extra = 1
    sortable_field_name = "order"
    inlines = [ComponentInline]


class RowInline(NestedTabularInline):
    model = Row
    extra = 1
    sortable_field_name = "order"
    inlines = [ColumnInline]


class ContainerInline(NestedStackedInline):
    model = Container
    extra = 1
    sortable_field_name = "order"
    inlines = [RowInline]


@admin.register(Page)
class PageAdmin(NestedModelAdmin):
    inlines = [ContainerInline]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Slider)
