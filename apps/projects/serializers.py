from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    # Mostra o status bonitinho ("Em Andamento") em vez de "active"
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    # Mostra o nome do dono, não o ID
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at']