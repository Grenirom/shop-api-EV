from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from apps.generals.send_mail import send_activation_email

from .serializers import RegisterSerializer

User = get_user_model()


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        if user:
            try:
                send_activation_email(email=user.email, code=user.activation_code)
            except Exception as e:
                return Response({
                    'msg': 'Во время отправки письма на почту возникла ошибка',
                    'data': serializer.data
                }, status=201)
            return Response(serializer.data, status=201)
        

class ActivateView(APIView):
    def get(self, request):
        activation_code = request.query_params.get('u')
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({
            'msg': 'Successfully activated your account'
        }, status=200)
    