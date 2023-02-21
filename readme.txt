env
install pakietow (django)
wygenerowanie aplikacji

python manage.py runserver

1. projektowanie modelu i utworzenie pliku migracyjnego
python manage.py makemigrations - models wszystkich apek

2. utworzenie tabeli
python manage.py migrate - migrations 

3. utworzenie superusera do panelu admina
python manage.py createsuperuser

aleksanderdudek
adud3k93@gmail.com 

4. rejestrowanie modelu w panelu admina (tutaj nie ma sensu migracja, tutaj wystarczy wrzucic kod)

URLS -> VIEWS (has access to database) -> TEMPLATES (has urls)

python -m pip install Pillow
modul pillow pozwala na obsluge zdjec