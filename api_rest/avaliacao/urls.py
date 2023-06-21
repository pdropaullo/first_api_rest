from django.urls import path
from .views import *

urlpatterns = [
    path('alunos/', AlunoAPIView.as_view(), name='alunos'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes')
]
