import machine

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    result = rightMin + (valueScaled * rightSpan)
    if result > 100:
        result = 100
    elif result < 0:
        result = 0
        
    return int(result)

def show_readings(pin):
    adc = machine.ADC(machine.Pin(pin))
    adc.atten(machine.ADC.ATTN_11DB) 
    adc.width(machine.ADC.WIDTH_11BIT)
    
    value = adc.read()
    
    return translate(value, 700, 1700, 100, 0)
