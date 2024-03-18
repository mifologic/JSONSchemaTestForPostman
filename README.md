# JSON Schema Test For Postman

Проект позволяет сгенерировать json-схему и тест для её проверки в Postman.

### Используемые библиотеки
* json (входит в стандартные библиотеки Python, не требует дополнительной установки);
* [requests](https://requests.readthedocs.io/en/latest/);
* [genson](https://github.com/wolverdude/GenSON).
---
## Запуск проекта локально
На компьютере должен быть установлен Python. Инструкция по установке: 
[Windows](https://metanit.com/python/tutorial/1.2.php),
[MacOS](https://metanit.com/python/tutorial/1.5.php),
[Linux](https://metanit.com/python/tutorial/1.6.php).

### Запуск из командной строки

Запустить терминал. Ввести команду, чтобы скопировать проект к себе на компьютер (будет скопирован в текущую папку):
```commandline
git clone https://github.com/mifologic/JSONSchemaTestForPostman.git
```

Также потребуется установить библиотеки, не входящие в стандартные. 
Используемые в проекте библиотеки описаны в файле *requirements.txt*.
Команда для установки:
````commandline
python -m pip install -r requirements.txt
````
**NB!** В некоторых операционных системах python может запускаться другой командой, например, python3. 

---
Проект запускается файлом start_schema_generator.py.
Также при запуске нужно передать:
* тип метода (поддерживаются GET, POST, PUT, PACTH);
* url;
* body (необязательный параметр).

Команда для запуска:
```commandline
python start_schema_generator.py GET https://yoururl.com
```

В ответ вернётся сгенерированный тест для Postam, который можно скопировать и добавить на вкладку Test для этого метода.

----
### Примеры, с помощью которых можно проверить работу проекта:
**GET-metod**:
```commandline
python start_schema_generator.py GET https://fakerestapi.azurewebsites.net/api/v1/Books
```
**POST-metod**:
```commandline
python start_schema_generator.py POST https://fakerestapi.azurewebsites.net/api/v1/Activities --body="{\"id\":0,\"title\":\"Activity 14\",\"dueDate\":\"2024-03-17T20:57:04.425Z\",\"completed\":false}"
```