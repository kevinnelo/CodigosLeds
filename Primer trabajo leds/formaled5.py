from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau

pleds=[2,4,16,17,5,18,19,21,3]
tleds=[]
for i in pleds:
    tleds.append(pin(i,pin.OUT))
print(tleds)

def derecha():
    for i in tleds:
        for j in range (3):
            i.value(not i.value())
        pausam(150)
        
def izquierda():
    for i in reversed (tleds):
        for j in range (3):
            i.value(not i.value())
        pausam(150)
        
while True:
    derecha()
    #izquierda()