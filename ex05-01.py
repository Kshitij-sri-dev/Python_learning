
tt=0.0
cc=0.0
while True:
    try:
        inp=input('Enter a number:')
        if inp=='done':
            print('Done')
            break
        else:
            inp=float(inp)
            tt=tt+inp
            cc=cc+1
    except:
        print('Invalid inp')
        continue


print(tt,cc,tt/cc)
