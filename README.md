**Инструкция по запуску приложения**
-
1) создать виртуальное окружение (python3 -m venv venv)
2) активировать виртуальное окружение (. venv/bin/activate)
3) скачать все библиотеки (pip install -r requirements.txt)
4) создать файл .env и заполнить данные в соответствии с файлом .env.example
5) создать базу данных (createdb shop_api_db)
6) провести миграции 1) ./manage.py makemigrations, 2) ./manage.py migrate
7) создать админа (./manage.py createsuperuser)