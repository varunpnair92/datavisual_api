from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Dataset, Entity, Detail
from .serializers import DatasetSerializer, EntitySerializer, DetailSerializer


# ----- Dataset Views -----
class DatasetListCreateView(generics.ListCreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


class DatasetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


# ----- Entity Views -----
class EntityListCreateView(generics.ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    parser_classes = [MultiPartParser, FormParser]  # ✅ allow file upload


class EntityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    parser_classes = [MultiPartParser, FormParser]  # ✅ allow file upload


# ----- Detail Views -----
class DetailListCreateView(generics.ListCreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer


class DetailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
