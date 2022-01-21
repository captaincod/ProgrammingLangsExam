"""
Написать программу, которая порождает два
потока: первый поток выводит четные числа в
диапазоне от 0 до 10, второй поток нечетные на
этом же диапазоне
"""
from threading import Thread
import time


def even():
    for i in range(1, 11):
        if i % 2 == 0:
            print(i)
            time.sleep(1)


def odd():
    for i in range(1, 11):
        if i % 2 != 0:
            print(i)
            time.sleep(1)


if __name__ == '__main__':

    th_even = Thread(target=even())
    th_odd = Thread(target=odd())
    th_even.run()
    th_odd.run()

