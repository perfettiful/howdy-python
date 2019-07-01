import time 
def countdown(n):
    while n > 0:
        n = n - 1
        print(n)
        time.sleep(1)
        
        if n % 2 == 0 :
            print('Every oudder! ' ,n)
countdown(50)