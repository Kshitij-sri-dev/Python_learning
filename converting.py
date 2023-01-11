hrs=input('Enter hours:')
rate=input('Enter rate:')
run_hrs=float(hrs)
run_rate=float(rate)
if run_hrs>40:
    wage=(40*run_rate)+((run_hrs-40)*run_rate*1.5)
elif run_hrs<=40:
    wage=run_hrs*run_rate
print('Pay:',wage)
