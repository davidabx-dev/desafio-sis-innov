from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    # Só quem tem login pode acessar (Requisito de segurança da vaga)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # O usuário só vê os projetos DELE
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Quando criar, o dono é automaticamente o usuário logado
        serializer.save(owner=self.request.user)