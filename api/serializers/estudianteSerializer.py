from rest_framework import serializers
from api.models import Estudiante
from api.serializers.epsSerializer import EpsSerializer
class EstudianteSerializer(serializers.ModelSerializer):
    id_eps = EpsSerializer(many=False, read_only=True)
    class Meta:
        model = Estudiante
        fields = ['identification','apellidos','nombres','direccion','telefono','correo','edad','id_eps','adulto','genero','activo','comentario']