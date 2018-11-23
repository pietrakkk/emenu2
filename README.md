# Emenu

Aplikacja do zarządzania kartami menu.

## Instalacja

Stwórz plik konfiguracyjny .env w katalogu /config, bądź skopiuj .env.example do .env

Stwórz środowisko:

```virtualenv venv -p python3```

Zainstaluj biblioteki:

```. venv/bin/activate && pip install -r requirements.txt```

Uruchom migracje:

```python manage.py migrate```


[Opcjonalnie] Załaduj dane testowe:

```python manage.py loaddata initial_data.json```


Uruchom aplikację:

```python manage.py runserver```


[Opcjonalnie] Uruchomienie testów + procentowy raport:

```coverage run --source='.' manage.py test && coverage report```
