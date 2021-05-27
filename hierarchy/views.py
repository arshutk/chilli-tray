from rest_framework.generics import ListAPIView
from hierarchy.models import AppModel
from hierarchy.serializers import AppModelSerializer


class HierarchyView(ListAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppModelSerializer

