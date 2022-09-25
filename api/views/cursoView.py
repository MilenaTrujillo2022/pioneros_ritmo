from email.policy import HTTP
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from api.models.curso import Curso
from api.serializers.cursoSerializer import CursoSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def curso_api_view(request):

    if request.method == 'GET':
        curso = Curso.objects.all()
        if curso:
            serializer = CursoSerializer(curso, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No se han encontrado cursos'},status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def curso_detail_api_view(request, pk= None):

    curso = Curso.objects.filter(id = pk).first()
    if curso == None:
        return Response({'message': 'No se ha encontrado el curso'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CursoSerializer(curso)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        curso.delete()
        return Response({'message': 'El curso fue eliminado'},status=status.HTTP_200_OK)