from threading import Thread
import time


def even():
    for i in range(1, 11):
        if i % 2 == 0:
            print(i)
            time.sleep(0.5)


def odd():
    for i in range(1, 11):
        if i % 2 != 0:
            print(i)
            time.sleep(0.5)


if __name__ == '__main__':

    th_even = Thread(target=even())
    th_odd = Thread(target=odd())
    th_even.start()
    th_odd.start()

