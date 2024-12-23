Задание №8 по выбору: Постфиксная запись
====
Студентка ИТМО, Коновалова Кира Романовна, 472066

Вариант 9
----

Задание
---
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения. Дано выражение в обратной польской записи. Определите его значение 


Input / Output
----

| Input         | Output |
|---------------|--------|
| 7             | -102   |
| 8 9 + 1 7 - * |        |



## Ограничения по времени и памяти

- Ограничение по времени. 2 сек.
- Ограничение по памяти. 256 мб.

## Структура проекта:

* task8/ - папка со всеми файлами для задачи
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
   cd algoritms_labs/lab4
   ```
3. Запустите все задачи лабораторной:
```bash
   python utils.py --tasks --lab lab4
   ```

## Тестирование
запустите все тесты лабораторной с помощью команды:
```bash
    pytest utils.py --tests --lab lab4
```
