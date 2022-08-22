from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau

leda=pin(2,pin.OUT)
ledb=pin(4,pin.OUT)
ledc=pin(16,pin.OUT)
ledd=pin(17,pin.OUT)
lede=pin(5,pin.OUT)
ledf=pin(18,pin.OUT)
ledg=pin(19,pin.OUT)
ledh=pin(21,pin.OUT)
ledi=pin(3,pin.OUT)

ledgrup=[leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi]

def derecha():
    for i in ledgrup:
        for j in range (2):
            i.value(not i.value())
            pausam(50)
            
def izquierda():
    for i in reversed(ledgrup):
        for j in range (2):
            i.value(not i.value())
            pausam(50)
            
while True:
    #derecha()
    izquierda()
    