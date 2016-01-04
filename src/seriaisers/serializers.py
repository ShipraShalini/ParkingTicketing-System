from rest_framework import serializers



class SlotSerializer(serializers.Serializer):
    slot_no = serializers.IntegerField(read_only=True)
    status = serializers.CharField(max_length=20)
    registration_no = serializers.CharField(max_length=20)
    colour = serializers.CharField(max_length=20)