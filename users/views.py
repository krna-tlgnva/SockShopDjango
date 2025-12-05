from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            'count': users.count(),
            'results': serializer.data
        })
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Пользователь успешно создан',
                    'user': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'message': 'Ошибка при создании пользователя',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {'message': 'Пользователь не найден'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def update(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'Пользователь успешно обновлен',
                    'user': serializer.data
                })
            return Response(
                {
                    'message': 'Ошибка при обновлении пользователя',
                    'errors': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response(
                {'message': 'Пользователь не найден'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def partial_update(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'Пользователь успешно обновлен',
                    'user': serializer.data
                })
            return Response(
                {
                    'message': 'Ошибка при обновлении пользователя',
                    'errors': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response(
                {'message': 'Пользователь не найден'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user_name = f"{user.first_name} {user.last_name}"
            user.delete()
            return Response({
                'message': f'Пользователь {user_name} успешно удален'
            })
        except User.DoesNotExist:
            return Response(
                {'message': 'Пользователь не найден'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if query:
            users = User.objects.filter(
                first_name__icontains=query
            ) | User.objects.filter(
                last_name__icontains=query
            ) | User.objects.filter(
                email__icontains=query
            )
        else:
            users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        return Response({
            'count': users.count(),
            'results': serializer.data
        })