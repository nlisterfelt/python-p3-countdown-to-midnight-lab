import time
def countdown(num):
    i=0
    while i<=num:
        if(i<num):
            print(f'{num-i} SECOND(S)!')
            i+=1
        elif(i==num):
            print('HAPPY NEW YEAR!')
            i+=1

def countdown_with_sleep(num):
    i=0
    while i<=num:
        time.sleep(1)
        if(i<num):
            print(f'{num-i} SECOND(S)!')
            i+=1
        elif(i==num):
            print('HAPPY NEW YEAR!')
            i+=1
