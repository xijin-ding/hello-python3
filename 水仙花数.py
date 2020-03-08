# 水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）

import time
for a in range(1, 10):
    time.sleep(0.01)
    print("\033[0;27;40m\t执行a循环\033[0m","第"+str(a)+"次")
    a1 = a ** 3
    for b in range(0, 10):
        time.sleep(0.01)
        print("\033[0;31;40m\t执行b循环\033[0m","第"+str(b)+"次")
        b1 = b ** 3
        for c in range(0, 10):
            c1 = c ** 3
            time.sleep(0.01)
            print("执行c循环","第"+str(c)+"次")
            if a1+b1+c1==a*100+b*10+c:
                print("\033[0;34;0m\t%d\033[0m" %(a*100+b*10+c))




