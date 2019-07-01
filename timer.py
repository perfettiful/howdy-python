import time 
def countdown(n):

    print('Ready! . . . ')
    time.sleep(1)
    print('. . . Set!')

    while n > 0:
        n = n - 1
        time.sleep(2)
        print(n)
        
        
        if n % 2 == 0 :
             print("Printin' all da evens indicies: %s." %n)
    
    if n == 0 :
        print('. . . ')

        time.sleep(3)
        print('***** =====================  *****')
        print('***** 100 DAYS OF CODE 2K19! *****')
        print('***** =====================  *****')
countdown(6)