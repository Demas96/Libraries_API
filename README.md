# API Libraries

Данный API парсит данные по библиотекам с сайта https://opendata.mkrf.ru.  
Поскольку в задании и API и база должны быть в одном образе, была выбрана база SQLite.  
Так же есть реализация с базой PostgreSQL через docker-compose.

## Основной стек

* DRF
* SQLite

## Запуск  

Образ выложен на https://hub.docker.com/, поэтому запустить можно командой

    docker run -p 8000:8000 demas96/lib_api_test

или скачать репозиторий, собрать и запустить образ.

# REST API

Чтобы загрузить данные с сайта https://opendata.mkrf.ru/ необходимо выполнить get запрос

`/api/parser`

Если данные были получены, то ответ будет
```json
{
    "status_code": 200,
    "added": 100
}
```
иначе вернется код ошибки.



Далее можно работать с данными через wed интерфейс  

`/api/v1/libraries/`

REST API описан ниже.

## Запросы

- GET `/api/v1/libraries/` - получение всех записей  


- GET `/api/v1/libraries/{id}` - получение записи по id


- GET `/api/v1/libraries/?search=` - общий поиск по записям


- GET `/api/v1/libraries/?name__icontains=&
description__icontains=&address__fullAddress__icontains=&
contacts__phones__icontains=&contacts__website__icontains=&
locale__name__icontains=` - одтельный поиск по полям записи, где параметры: 

  `name__icontains=` название библиотеки;  
  `description__icontains=` описание библиотеки;  
  `address__fullAddress__icontains=` адрес библиотеки;  
  `contacts__phones__icontains=` телефон библиотеки;  
  `contacts__website__icontains=` сайт библиотеки;  
  `locale__name__icontains=` локация библиотеки.

В данном API для адреса, локации и контактов в БД реализованы отдельные модели,
связанные с моделью библиотеки, но на данном этапе по API реализована работа только
с моделью библиотеки.

- POST `/api/v1/libraries/` - создать запись (запрос с телом в формате JSON)  

```json
{
    "name": str,
    "description": str,
    "image": str
}
```

- PATCH `/api/v1/libraries/{id}` - изменить запись по id (запрос с телом в формате JSON)  

```json
{
    "name": str,
    "description": str,
    "image": str
}
```
- DELETE `/api/v1/libraries/{id}` - удалить запись по id


## Ответ
Ответом на запросы будут в формате JSON
```json
[
    {
        "id": int,
        "name": str,
        "description": str,
        "image": str,
        "address": {
            "id": int,
            "street": str,
            "fullAddress": str
        },
        "contacts": {
            "id": int,
            "website": str,
            "phones": str
        },
        "locale": {
            "id": int,
            "name": str,
            "timezone": str
        }
    },
]
```

