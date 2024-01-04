from django.urls import path
from .views import CategoryList,CategoryDetails,BlogList,BlogDetails
urlpatterns = [
    path('blogs/',BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetails.as_view(), name='blog-details'),
    path('category/',CategoryList.as_view(),name='category-list'),
    path('category/<int:pk>/', CategoryDetails.as_view(), name='category-details')
]
