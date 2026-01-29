from django.db import models
from user.models import Timestamp


class Page(Timestamp):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'


class Container(Timestamp):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='containers')
    title = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or f"Container {self.id}"

    class Meta:
        ordering = ['order']
        verbose_name = 'Container'
        verbose_name_plural = 'Containers'


class Row(Timestamp):
    container = models.ForeignKey(Container, on_delete=models.CASCADE, related_name='rows')
    title = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or f"Row {self.id}"

    class Meta:
        ordering = ['order']
        verbose_name = 'Row'
        verbose_name_plural = 'Rows'


class Column(Timestamp):
    row = models.ForeignKey(Row, on_delete=models.CASCADE, related_name='columns')
    title = models.CharField(max_length=255, blank=True, null=True)
    width = models.PositiveIntegerField(default=12, help_text="Grid width from 1 to 12")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or f"Column {self.id}"

    class Meta:
        ordering = ['order']
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'


class Component(Timestamp):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='components')
    title = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.CharField(max_length=50, choices=[
        ('text', 'Text'),
        ('image', 'Image'),
        ('button', 'Button'),
        ('video', 'Video'),
        ('html', 'Custom HTML'),
    ], default='text')
    content = models.TextField(blank=True, null=True, help_text="Text content or HTML")
    image = models.ImageField(upload_to='components/images/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or f"{self.get_content_type_display()} Component {self.id}"

    class Meta:
        ordering = ['order']
        verbose_name = 'Component'
        verbose_name_plural = 'Components'


class Slider(Timestamp):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, default='')
    button_text = models.CharField(max_length=255, blank=True, null=True, default='')
    button_url = models.URLField(blank=True, null=True, default='')
    image = models.ImageField(upload_to='sliders', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
