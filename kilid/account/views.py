
from rest_framework.response import Response
from .serializers import CustomUserSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .models import CustomUser
from rest_framework.filters import SearchFilter,OrderingFilter
   

class GetListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class =CustomUserSerializers
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('size','my_name')


