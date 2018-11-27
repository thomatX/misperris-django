from .models import Usuario, Rescatado
from rest_framework import serializers

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email','rut','nombre','fecha_nacimiento','numero_telefono','region','comuna','tipo_casa','password')

class RescatadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rescatado
        fields = ('nombre','raza','descripcion','state')