hrs=input('Enter hours:')
rate=input('Enter rate:')
rh=float(hrs)
rr=float(rate)

def money(hrs, rate):
    if rh>40:
        wage=(40*rr)+((rh-40)*rr*1.5)
    elif rh<=40:
        wage=rh*rr
    print('Returning',wage)
    return wage

try:
    xp=money(hrs, rate)
    print('Pay:',xp)
except:
    print('Error, please enter numeric value')
