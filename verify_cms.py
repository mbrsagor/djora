import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djora.settings')
django.setup()

from backend.models import Page, Container, Row, Column, Component
from backend.serializers import PageSerializer

def run_verification():
    print("Creating test data...")
    # Clean up previous test data
    Page.objects.filter(slug='test-page').delete()

    # Create Page
    page = Page.objects.create(title="Test Page", slug="test-page", content="Legacy Content")
    
    # Create Container
    container = Container.objects.create(page=page, title="Hero Section", order=1)
    
    # Create Row
    row = Row.objects.create(container=container, title="Main Row", order=1)
    
    # Create Column
    col1 = Column.objects.create(row=row, title="Left Column", width=6, order=1)
    col2 = Column.objects.create(row=row, title="Right Column", width=6, order=2)
    
    # Create Components
    Component.objects.create(column=col1, title="Headline", content_type="text", content="<h1>Hello World</h1>", order=1)
    Component.objects.create(column=col2, title="Image", content_type="image", order=1)

    print("Data created successfully.")

    # Test Serializer
    print("Testing Serializer...")
    serializer = PageSerializer(page)
    data = serializer.data
    
    # Verify structure
    assert data['slug'] == 'test-page'
    assert len(data['containers']) == 1
    assert data['containers'][0]['title'] == 'Hero Section'
    assert len(data['containers'][0]['rows']) == 1
    assert len(data['containers'][0]['rows'][0]['columns']) == 2
    assert len(data['containers'][0]['rows'][0]['columns'][0]['components']) == 1
    
    print("Serializer output:")
    print(json.dumps(data, indent=2))
    print("\nVERIFICATION SUCCESSFUL!")

if __name__ == "__main__":
    run_verification()
