from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario

class ComentarioSerializer(ModelSerializer):
    model: Comentario
    fields: (
        'id',
        'comentario',
        'data',
        'aprovado'
    )