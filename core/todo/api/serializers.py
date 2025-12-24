from rest_framework import serializers
from todo.models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    absolut_url = serializers.SerializerMethodField('get_absolut_url')

    class Meta:
        model = Task
        fields = ['id','author' ,'task', 'absolut_url', 'start_date', 'end_date']
        read_only_fields = ['author']

    # Create task only for request.user
    def create(self, validated_data):
        validated_data['author'] = User.objects.get(id=self.context.get('request').user.id)
        return super().create(validated_data)
    
    # Link for task detail
    def get_absolut_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.id)
    