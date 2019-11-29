from django.urls import path

from .views import ShowImagesView,CreateImagesView

urlpatterns = [
    path('', ShowImagesView.as_view(), name='showimages'),
    path('images/', CreateImagesView.as_view(), name='add_images') 
    
]
