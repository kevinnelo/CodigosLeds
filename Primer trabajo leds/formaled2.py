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

def print_led(a,b,c,d,e,f,g,h,i):
    leda.value(a)
    ledb.value(b)
    ledc.value(c)
    ledd.value(d)
    lede.value(e)
    ledf.value(f)
    ledg.value(g)
    ledh.value(h)
    ledi.value(i)
    pausam(200)

while True:
    print_led(1,0,0,0,0,0,0,0,1)
    print_led(0,1,0,0,0,0,0,1,0)
    print_led(0,0,1,0,0,0,1,0,0)
    print_led(0,0,0,1,0,1,0,0,0)
    print_led(0,0,0,0,1,0,0,0,0)