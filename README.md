
#DZ_3
# Конвертер JSON в учебный конфигурационный язык (УКЯ)


## Возможности
- Конвертация JSON в УКЯ.
- Поддержка сложных вложенных структур.
- Преобразование массивов, словарей, строк и чисел.
- Удобный для чтения результат.


### Описание основных файлов:
- **`script.py`** — Основной скрипт, выполняющий преобразование JSON в УКЯ.
- **`config_1.json`** — Тестовый пример с конфигурацией веб-приложения.
- **`config_2.json`** — Тестовый пример с конфигурацией базы данных.
- **`README.md`** — Описание проекта.
- **`Script_For_Start.txt`** — Скрипт для запуска приложения из командной строки.

## Установка

1. Клонируйте репозиторий:
```bash
   git clone https://github.com/your-username/json-to-custom-lang.git
   cd json-to-custom-lang
```
Убедитесь, что у вас установлен Python версии 3.6 или выше.

Если проект требует дополнительных библиотек, установите их:

bash
Copy code
```bash
pip install -r requirements.txt
```
### Использование
Запустите скрипт, указав путь к JSON-файлу в качестве аргумента командной строки:

bash
Copy code
```bash
python script.py <путь_к_JSON_файлу>
```
Пример
Для файла config.json с содержимым:

json
Copy code
```bash
{
    "app": "WebServer",
    "port": 8080,
    "endpoints": [
        "/api/v1/resource",
        "/api/v1/status"
    ]
}
```
Запустите команду:

bash
Copy code
```bash
python script.py config.json
```
Скрипт выведет результат:

```bash
{
 app -> "WebServer".
 port -> 8080.
 endpoints -> ( "/api/v1/resource", "/api/v1/status" ).
}
```
Формат учебного конфигурационного языка (УКЯ)
#### Массивы
Записываются в виде:

```bash
( значение1, значение2, значение3, ... )
```
#### Словари
Записываются в виде:

```bash
{
 ключ -> значение.
 ключ -> значение.
 ...
}
```
#### Строки
Обрамляются двойными кавычками:

```bash
"Это строка"
```
#### Числа
Записываются без изменений:

```bash
42
```
#### Константы
Могут быть объявлены и вычислены:

```bash
имя = значение;
#[имя]
```
## Примеры
### Пример 1: Конфигурация веб-приложения
Входной JSON:

json
Copy code
```bash
{
    "app": "WebServer",
    "port": 8080,
    "endpoints": [
        "/api/v1/resource",
        "/api/v1/status"
    ]
}
```
### Результат:

```bash
{
 app -> "WebServer".
 port -> 8080.
 endpoints -> ( "/api/v1/resource", "/api/v1/status" ).
}
```
### Пример 2: Конфигурация базы данных
Входной JSON:

json
Copy code
```bash
{
    "db": {
        "type": "postgres",
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "user": "admin",
            "password": "secret"
        }
    }
}
```
### Результат:

```bash
{
 db -> {
  type -> "postgres".
  host -> "localhost".
  port -> 5432.
  credentials -> {
   user -> "admin".
   password -> "secret".
  }
 }.
}
```
