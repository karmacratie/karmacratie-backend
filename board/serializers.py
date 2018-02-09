from board.models import Ministry, Cycle
from rest_framework import serializers


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = ( 'name', 'description', 'admin' )

class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle 
        fields = ( 'type', 'start_date', 'end_date', 'active', 'next_cycle' ) 
