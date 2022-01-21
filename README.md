# Задания экзамена

1. Расстояние между точками  
   - Реализовать тип данных для измерения длины пути по произвольному последовательному набору точек 
   - Демонстрация в `/distance_meter_1/DistanceMeter.py`

2. Разбор на токены  
   - Написать программу для разбора на токены следующих выражений:  
     ```c++
     int value = 10;
     int* ptr = &value;
     ```
   - Демонстрация в `/token_parser_2/TokenParser.py`

3. Потоки  
   - Написать программу, которая порождает два потока: первый поток выводит четные числа в диапазоне от 0 до 10, второй поток нечетные на этом же диапазоне 
   - Демонстрация в `/parity_threads_3/ParityThreads.py`


4. Вывод объекта  
   - Реализовать функцию func так, чтобы если в функцию передан объект типа A, было выведено его значение, если передан объект B, то бросить исключение ObjectException, во всех остальных случаях напечатать объект в виде строки  
   - Пример на Kotlin:  
     ```kotlin
      class A(val value: Int)
      class B(val value: Double)
      fun func(obj: Any) { }
      fun main() {
         func(A(10));
         func(B(1.5));
         func("hello!");
      }
     ```
   - Демонстрация в `/print_object_4/PrintObject.py`

6. Тесты  
   - Написать тесты для предложенного класса
   - `/tests_6`
   - Покрытие тестами:
     
     ![coverage_report](https://user-images.githubusercontent.com/46486971/150045121-e1a5994e-e1b1-465a-bebd-633b663d4be9.png)
