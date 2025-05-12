from rest_framework import serializers
from Blog.models import BlogPost, CustomUser

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = BlogPost
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

