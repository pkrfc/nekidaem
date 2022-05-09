### Описание проекта:

```
API блога "nekidaem"
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/pkrfc/nekidaem.git
```

```
cd nekidaem
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:


```
Запрос:
GET http://127.0.0.1:8000/api/v1/posts/1/
Ответ:
{
    "id": 1,
    "author": "admin",
    "views_user": "Maxim",
    "title": "1",
    "text": "test",
    "pub_date": "2022-05-08T13:24:34.865203Z"
}
```

```
Запрос:
PUT http://127.0.0.1:8000/api/v1/posts-list/2/
Ответ:
{
    "id": 2,
    "text": "test2",
    "title": "2",
    "author": 1,
    "views_user": 2
}

```
