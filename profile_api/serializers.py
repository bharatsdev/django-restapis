from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializer a filed for testing a APIView"""
    name = serializers.CharField(max_length=100)
