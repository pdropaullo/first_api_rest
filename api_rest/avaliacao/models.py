from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.CharField(max_length=255)
    avaliacao = models.TextField()
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Avaliações"
        unique_together = ['professor', 'aluno']

    def __str__(self):
        return self.professor
