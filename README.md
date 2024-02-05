# fastAPI_SQL

## Навчальний проект 

### з дисципліни "Бази даних"

Проект розроблено у формі веь додатку з використанням  
 - бази даних MySQL;
 - Python-фреймворку FastAPI;
 - HTML, CSS, JS в якості клієнського інтерфейсу.

Додаток складається з 3 частин:

-   сервіс бази даних, який повинен
    - бути запущений, 
    - містити базу даних з заповненими таблицями,
    - налаштованого користувача з правами доступу до бази.

    - Для отримання доступу до бази даних необхідні:
        - адреса сервісу (localhost);
        - ім'я користувача;
        - його пароль;
        - назва бази даних.

- бекенд з API (Application Programming Interface);
- фронтенд, який реалізовано у вигляді простого HTML з JS.

#### Детальніше про бекенд:

FastAPI — веб-фреймворк для створення API, написаний на Python. Один із найшвидших та найпопулярніших 
(після Django и Flask) веб-фреймворків, написаних на Python (на 2023 рік).
Перевагою є вбудований сервіс створення документації на базі Swagger.

Бекенд не залежить від бази даних (дані користувача, назви бази даних, таблиць і т.п.)

Особливості запуску скрипту Python:

Загальні відомості: [Wiki](https://uk.wikipedia.org/wiki/Python)

Це скриптова інтерпретована мова. Для запуску в системі повинен бути встановлений інтерпретатор. Тобто,
запуск з командного рядка відбувається у форматі: "python my_program.py", де python - назва інтерпретатора, 
встновленого в системі, my_program.py - назва скрипта.

Перед початком потрібтно перевірити наявність інтерпретатора в системі, за потреби - його встановити.

В середовищі Windows python може бути встановлений і викликатись ("py" або "python").
[Microsoft tutorial](https://learn.microsoft.com/en-us/windows/python/beginners#hello-world-tutorial-for-some-python-basics)

Якщо встановлений, результатом буде:
```bash
osiko@homeamd ~ ❯❯❯ py
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Це вже працюючий інтерпретатор в якому можна виконувати код Python, або
```python
>>> 3+2
5
>>>
```
Вийти: Ctrl+z, Enter

В середовищі Linux встановлений майже завжди, але може відгукуватись на "python3".

Для Windows, якщо не встановлений, - встановити зі сторінки [Python](https://www.python.org/downloads/).

Python здобув свою славу і популярність переважно завдяки величезній кількості бібліотек, 
які дозволяють виконувати завдання від створення навчальних ігор [pygame](https://www.pygame.org/docs/) 
до наукових інструментів [pythonforthelab](https://pythonforthelab.com/).
Більшість цих бібліотек можна знайти на [Pypi](https://pypi.org/). Для їх встановлення існує інстурмент "pip".
Основи використання: [pip usage](https://pip.pypa.io/en/stable/user_guide/).
Зворотною стороною такого різномаїття стала необхідність використання віртуальних середовищ. Справа у тому, 
що різні бібліотеки можуть викристовувати різні версії Python, які не завжди сумісні. Тому для окремих 
проектів прийнято використовувати окремі віртуальні середовища.
Напоширенішим  є проект venv [venv](https://docs.python.org/3/library/venv.html), 
трохи простіше: [www.geeksforgeeks.org](https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/)
Основні кроки:
- в папці проекту запустити ```python -m venv ./venv``` (-m дозволяє виконувати скрипт без вказівки повного шляху 
до нього, за умови, що він імпортований як модуль; venv - програма для створення віртуального середовища; 
"./venv" - місце, де будуть розташовані файли середовиша.)
- з папки "venv\Scripts" запустити скрипт "activate.bat". Загальна команда: ```venv\Scripts\activate.bat```.
Ознакою успіху буде зміна запрошення командного рядка: має додатись ```(venv_name)$```. 
(Для виходу достатньо команди ```deactivate```.)
- При активованому середовищі можна встановлювати залежності проекту і запсускати скрипти Python.

Отже, для цього проекту кроки наступні:
- в терміналі перейти у папку ```backend```;
- ```python -m venv ./venv```;
- ```venv\Scripts\activate.bat```;
- ```pip install -r requrements.txt```; (встановляться усі залежності, перелічені у файлі requrements.txt)
- поряд з файлом requirements.txt севорити файл ".env" до якого прописати дані своєї бази даних у форматі:
```dotenv
DB_HOST="locslhost"
DB_USER="sql_user"
DB_PASSWORD="password"
DB_NAME="carshop"
```
- після цього виконати: ```python -m uvicorn app.main:app --reload```; 
У разі успіху маєте побачити щось схоже:
```bash
osiko@homeamd D:\GitHubD\kpi-db\fastAPI_SQL\backend git:for_public   backend 3.11.4 ❯❯❯ python -m uvicorn app.main:app --reload 
INFO:     Will watch for changes in these directories: ['D:\\GitHubD\\kpi-db\\fastAPI_SQL\\backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [56736] using WatchFiles
INFO:     Started server process [56896]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:51574 - "GET / HTTP/1.1" 200 OK
```
Серед написаного, "http://127.0.0.1:8000" - це базова адреса API. Побачити щось ікавіше можна заадресою:
"http://127.0.0.1:8000/docs". Сама точка доступу за адресою "http://127.0.0.1:8000/api/sql/"  - надсилаючи 
сюди sql запити, можна отримувати дані з бази, наприклад за допомогою JS:
```javascript
async function getSiteData(query) {
    let source = "http://127.0.0.1:8000/api/sql/";
    const response = await fetch(source, {
        method: 'POST',
        body: query
    });
    const { data } = await response.json();
    let site_data = await data;
    return site_data
  }
```
у наведеному коді змінна ```query``` це строка виду 
```sql 
SELECT * FROM car;
```
Отримаємо ```site_data```  у вигляді:
```json
{
  "data": [
    {
      "id": 1,
      "brand": "ZAZ Slavuta",
      "made_in": "Україна",
      "delivery_date": "2012-01-02",
      "amount": 100,
      "price": 50001
    },
    {
      "id": 17,
      "brand": "Acura TLX",
      "made_in": "США",
      "delivery_date": "2012-01-02",
      "amount": 10,
      "price": 250000
    } ...
```