
def loopp():
    while True:
        inp=input('Enter a number:')
        try:
            if inp=='done':
                print('Done')
                break
            else:
                inp=float(inp)
                global tt
                global cc
                tt=tt+inp
                cc=cc+1
                continue
        except:
            print('Invalid input try again')
            continue


tt=0.0
cc=0.0
loopp()
print(tt,cc,tt/cc)
