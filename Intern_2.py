
def getFloat():
    while True :
        numfloat=float(input('Input Number : '))
        if float(numfloat) == 1.0:
            return int(numfloat)
        elif isinstance(numfloat,str):
            print( "Your enter Text")
        elif 0 <= int(numfloat) <= 10:
            return float(numfloat)
        else :
            print( "Your enter number more than 10 or less than 1")
            
def isPrime(num):
    totext = str(num).replace('.','')
    numberint = int(num)
    floatP = str(numberint)
    for t in range(len((str(numberint))),len(totext)) :
        if t == 4 : return False
        floatP += str(totext[t])
        print(floatP)
        for i in range(2,int(floatP)):
            if int(floatP) % i == 0 :
                break
        else : 
            return True
    else :
        return False

while True :
    num = getFloat()
    if num == 0 :
        break
    print(isPrime(num)) 
    
   
     
