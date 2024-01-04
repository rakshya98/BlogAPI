from .models import Blog,Category
from .serializers import BlogSerializer,CategorySerializer
from rest_framework import generics

class CategoryList(generics.ListCreateAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class BlogList(generics.ListCreateAPIView):
    serializer_class=BlogSerializer
    
    def get_queryset(self):
            queryset=Blog.objects.all()
            category=self.request.query_params.get('category_name')
            if category is not None:
                  queryset=queryset.filter(category=category)
            return queryset

class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=BlogSerializer
    queryset=Blog.objects.all()







