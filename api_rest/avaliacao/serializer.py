from rest_framework import serializers
from .models import *


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'matricula', 'data_criacao']


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'aluno', 'professor',
                  'avaliacao', 'nota', 'data_criacao']
