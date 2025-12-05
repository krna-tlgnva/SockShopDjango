from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'age', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_age(self, value):
        if value < 0 or value > 150:
            raise serializers.ValidationError("Age")
        return value
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            if self.instance and self.instance.email == value:
                return value
            raise serializers.ValidationError("User already exist")
        return value