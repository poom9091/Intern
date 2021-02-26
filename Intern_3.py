import random

def randomNumber():
    fivenum =[]
    listrandom = ''
    for i in range(5):
        fivenum.append(random.randint(0,9))
    for n in range(12):
        listrandom += str(fivenum[random.randint(0,4)])
    # แสดงคำตอบ
    # print(listrandom)
    return listrandom

def inputnum(listnumber) :
    count=0
    listout=[]
    lineinput=''
    for x in range(12) : listout.append('_')
    for i in range(1,6):
        while True :
            try:
                innum = int(input(('Round '+str(i)+' :')))
                if 0<=innum<=9 : break
                else : print( "You enter less than 0 or more than 9")
            except: print( "Your enter Text")
        for n in range(len(listnumber)):
            if str(innum) == listnumber[n]:
                count+=1
                listout[n] = innum
        lineinput += str(innum)
        for y in listout: print(y,end=' ')
        print(" : "+lineinput)
    return count

listnumber = randomNumber()
for  i in listnumber : print('_',end=' ') 
print('')
count = inputnum(listnumber)
print(count)