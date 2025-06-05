# import required module
from playsound import playsound

# playsound('record_out.wav')
num=input("enter a number between 1 and 999: ")
num=int(num)

if(num-(num%100)!=0):
    playsound(f'{int(num/100)}.wav')
    playsound(f'hundred.wav')
num=num%100
if(num<=20):
    playsound(f'{num}.wav')
    print('playing sound using  playsound')
    
else:
    i=num%10
    playsound(f'{num-i}.wav')
    if(i!=0):
        playsound(f'{i}.wav')