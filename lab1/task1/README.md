Задача 1. Сортировка вставками.
================================
Описание:
--------------------------------
В данной задаче реализуется алгоритм сортировки вставками. Алгоритм осуществляет сортировку путем перебора элементов массива слева направо, и при этом, размещает каждый следующий элемент таким образом, чтобы он оказался на правильной позиции между ближайшими элементами с минимальным и максимальным значением.

Формат входных данных:
------------------------------
* входные файлы находяться в файле input.txt
* в первой строке входного файла содержиться число n (1 <= n <= 10**3) - число элементов массива
* во второй строке находяться n различных целых чисел, по модулю не превосходящих 10**9

Формат выходных данных:
--------------------
* выходные данные находяться в файле output.txt
* данные файл должен содержать одну строку с отсортированным массивом. между любыми двумя числами должен стоять ровно один пробел

Ограничения:
--------
* ограничение по времени. 2 сек.
* ограничение по памяти. 256 мб

Структура проекта:
-------
* task1/ - папка со всеми файлами для задачи
* src/ - исходный код программы
    * input.txt - файл с входными данными
    * output.txt - файл с выходными данными
* tests/ - тестирование алгоритма

Код задачи:
---------
```
'''Задание 1. Сортировка вставкой'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, massive = f.readlines()
    array = insertion_sort(list(map(int, massive.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)
```

Запуск проекта
--------
1. перейдите в директорию src
2. вставте корректные данные в файл input.txt (или убедитесь что он содержит корректные данные)
3. запустите скрипт ```python isertion_sort.py```
4. результат выполнения кода будет в файле output.txt

Тестирование
----------
для проверки работы алгоритма выполняються тесты, находящиеся в директории tests в файле insertion_sort_test

```
import unittest

from lab1.task1.src.isertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

if __name__ == '__main__':
    unittest.main()
```