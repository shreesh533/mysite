from rest_framework.serializers import ModelSerializer
from consumer.models import User

class UserSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone']
