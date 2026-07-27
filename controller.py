from machine import Pin, ADC
import time

btn1 = Pin(5, Pin.IN) #D2
btn2 = Pin(6, Pin.IN) #D3
btn3 = Pin(7, Pin.IN) #D4
btn4 = Pin(8, Pin.IN) #D5
JSvolts = Pin(9, Pin.OUT) #D6
JSvolts.value(1)

adc1 = ADC(Pin(1)) #A0
adc1.atten(ADC.ATTN_11DB)

adc2 = ADC(Pin(2)) #A1
adc2.atten(ADC.ATTN_11DB)

counter = 0

while True:
    btn1val = btn1.value()  # Read the pin state (0 or 1)
    btn2val = btn2.value()
    btn3val = btn3.value()
    btn4val = btn4.value()
    YvalRaw = adc1.read_u16() #0 to 65535
    XvalRaw = adc2.read_u16() #0 to 65535
    
    Yval = YvalRaw*0.0041766 - 129
    Xval = XvalRaw*0.0041766 - 129
    
    print("Btn 1 State:", btn1val, "Btn 2 State:", btn2val, "Btn 3 State:", btn3val, "Btn 4 State:", btn4val, "Y value:", Yval, "X value:", Xval)
    time.sleep(0.1)       # Wait for 0.5 seconds before reading again
    print(counter)
    if(btn1val == 1 and btn2val == 1):
        counter+=1
        if(counter == 5):
            print("Controls switched")
    else:
        counter = 0
        
        
    
        
    
    
        
    