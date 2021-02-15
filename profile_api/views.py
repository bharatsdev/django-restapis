from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers


class HelloApiView(generics.GenericAPIView):
    """Test API View"""
    # serializer_class = serializers.HelloSerializer
    serializer_classes = serializers.HelloSerializer
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView Features"""

        an_view = [
            'Uses HTTP methods as function (get, post, delete,put, patch)',
            'Is similar to traditional DjangoView',
            'Give you the most  control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello Django', 'an_view': an_view})

    def post(self, request):
        """
        Create hello message with our  name
         param2 -- A second parameter
        """
        print(request.data)
        serializer = self.serializer_classes(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello Good Morning! {name}'
            return Response({'data': message}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handling  updating a object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handling partial update for an object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handling partial update for an object"""

        return Response({'method': 'PATCH'})


class HelloViewSets(viewsets.ViewSet):
    """Test api viewsets"""

    def list(self, request):
        """Return a hello method"""
        a_viewsets = [
            'User actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to urls using Routers',
            'Provides more functionality with less code ',
        ]

        return Response({'message': 'Hello world form ViewSets', 'a_viewsets': a_viewsets})
