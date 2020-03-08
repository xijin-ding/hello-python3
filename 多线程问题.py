import threading
import time


def test1():
    while True:
        print("线程1")
        time.sleep(1)


def test2():
    while True:
        print("线程2")
        time.sleep(1)



if __name__ == '__main__':
    t1 = threading.Thread(target=test1)  # 设置为线程
    t1.start()  # 开启线程

    t2 = threading.Thread(target=test2) # 设置为线程
    t2.start() # 开启线程

for i in range(5):
    print("liunx is good")
    time.sleep(1)


