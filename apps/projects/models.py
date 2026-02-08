from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    STATUS_CHOICES = [
        ('planning', 'Em Planejamento'),
        ('active', 'Em Andamento'),
        ('completed', 'Concluído'),
    ]

    name = models.CharField("Nome do Projeto", max_length=255)
    description = models.TextField("Descrição Técnica")
    client_name = models.CharField("Cliente", max_length=100)
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Projeto de Inovação"
        verbose_name_plural = "Projetos de Inovação"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"