from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.estudiante import Estudiante
from api.serializers.estudianteSerializer import EstudianteSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def estudiante_api_view(request):

    if request.method == 'GET':
        estudiante = Estudiante.objects.all()
        if estudiante:
            serializer = EstudianteSerializer(estudiante, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No se han encontrado estudiantes'},status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def estudiante_detail_api_view(request, pk= None):

    estudiante = Estudiante.objects.filter(id = pk).first()
    if estudiante == None:
        return Response({'message': 'No se ha encontrado el estudiante'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EstudianteSerializer(estudiante)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = EstudianteSerializer(estudiante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        estudiante.delete()
        return Response({'message': 'El estudiante fue eliminado'},status=status.HTTP_200_OK)