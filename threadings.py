import threading
import time


def eat_brackfast():
    time.sleep(3)
    print("finish eating brackfast")


def drink_tea():
    time.sleep(2)
    print("finish drinking tea")


def study():
    time.sleep(5)
    print("finish studying")


thread_1 = threading.Thread(target=eat_brackfast, args=())
thread_1.start()
thread_2 = threading.Thread(target=drink_tea, args=())
thread_2.start()
thread_3 = threading.Thread(target=study, args=())
thread_3.start()
