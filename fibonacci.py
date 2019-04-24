import time

num1 = 0
num2 = 1

while True:
    print(num1)
    # time.sleep(1)
    num1 += num2
    print(num2)
    # time.sleep(1)
    num2 += num1
