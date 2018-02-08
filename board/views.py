from rest_framework import viewsets
from board.models import Ministry, Cycle
from board.serializers import MinistrySerializer, CycleSerializer

# Create your views here.
class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.all().order_by('name')
    serializer_class = MinistrySerializer


class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all().order_by('name')
    serializer_class = CycleSerializer
