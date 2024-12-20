Задача 6. Пузырьковая сортировка
================================
Описание:
--------------------------------
В данной задаче реализуется алгоритм пузырьковой сортировки. Данный алгоритм последовательно сравнивает значения соседних элементов и меняет числа местами, если предыдущее число оказывается больше последующего. 

Формат входных данных:
------------------------------
* входные файлы находяться в файле input.txt
* в первой строке входного файла содержиться число n (1 <= n <= 1000) - число элементов массива
* во второй строке находяться n различных целых чисел, по модулю не превосходящих 10**9

Формат выходных данных:
--------------------
* выходные данные находяться в файле output.txt и представляют собой отсортированный массив
  
Ограничения:
--------
* ограничение по времени. 2 сек.
* ограничение по памяти. 256 мб

Структура проекта:
-------
* task6/ - папка со всеми файлами для задачи
* src/ - исходный код программы
    * input.txt - файл с входными данными
    * output.txt - файл с выходными данными
* tests/ - тестирование алгоритма

Код задачи:
---------
```
'''Задание 6. Пузырьковая сортировка.'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, mas = f.readlines()
    array = bubble_sort(list(map(int, mas.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)
```

Запуск проекта
--------
1. перейдите в директорию src
2. вставте корректные данные в файл input.txt (или убедитесь что он содержит корректные данные)
3. запустите скрипт ```python bubble_sort.py```
4. результат выполнения кода будет в файле output.txt

Тестирование
----------
для проверки работы алгоритма выполняються тесты, находящиеся в директории tests в файле test_bubble_sort.py

```
import unittest
from lab1.task6.src.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

if __name__ == '__main__':
    unittest.main()
```


