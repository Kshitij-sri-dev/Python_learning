str='X-DSPAM-Confidence: 0.8475'
lol=str.find(':')
print(lol)
olo=str[lol+1:]
print(olo)
value=float(olo)
print(value)
print(value+42)
