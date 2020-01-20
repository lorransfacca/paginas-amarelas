from rest_framework import serializers
from lista_telefonica.models import Contato, Anuncio

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['nome', 'telefone', 'email']

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = ['nome', 'descricao', 'telefone', 'valor']      