from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.eps import Eps
from api.serializers.epsSerializer import EpsSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def eps_api_view(request):

    if request.method == 'GET':
        eps = Eps.objects.all()
        if eps:
            serializer = EpsSerializer(eps, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No se han encontrado eps'},status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = EpsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def eps_detail_api_view(request, pk= None):

    eps = Eps.objects.filter(id = pk).first()
    if eps == None:
        return Response({'message': 'No se ha encontrado la eps'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EpsSerializer(eps)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = EpsSerializer(eps, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        eps.delete()
        return Response({'message': 'La eps fue eliminada'},status=status.HTTP_200_OK)