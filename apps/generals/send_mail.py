from django.core.mail import send_mail


def send_activation_email(email, code):
    activation_url = f'http://localhost:8000/api/account/activate/?u={code}'

    send_mail(
        'Здравствуйте! Активируйте ваш аккаунт',
        'Для активации аккаунта, перейдите по ссылке ниже:'
        f'\n{activation_url}',
        'ngrebnev17@gmail.com',
        [email],
        fail_silently=False
    )