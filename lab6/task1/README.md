Задание №1 по выбору: Множество
====
Студентка ИТМО, Коновалова Кира Романовна, 472066

Вариант 9
----

Задание
---
Реализуйте множество с операциями «добавление ключа», «удаление ключа»,
«проверка существования ключа».

Input / Output
----

| Input      | Output     |
|------------|------------|
| 8          | Y |
| A 2 | N |
| A 5 | N |
| A 3 |  |
| ? 2 |  |
| ? 4 |  |
| A 2 |  |
| D 2 |  |
| ? 2 |  |




## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.

## Структура проекта:

* task1/ - папка со всеми файлами для задачи
* src/ - исходный код программы
* tests/ - тестирование алгоритма
* txtf / - текстовые файлы с входными и выходными данными

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/repository-name.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algoritms_labs/lab6
   ```
3. Запустите все задачи лабораторной:
```bash
   python utils.py --tasks --lab lab6
   ```

## Тестирование
запустите все тесты лабораторной с помощью команды:
```bash
    pytest utils.py --tests --lab lab6
```