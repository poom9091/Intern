def InputUniverSity(numcount):
    ListName = []
    for i  in range(numcount):
        Upper = ""
        intput = input(('Input UniverSity ' +str(i+1)+ ' : '))
        for i in range(len(intput)):
            if intput[i].isupper() :
                if intput[i-1] == ' ' or i == 0:
                    Upper += intput[i]
        ListName.append({'Name':str(intput),'lenght':len(Upper),'Upper':str(Upper)})
    return ListName

while True :
    try :
        numcount = int(input('Number Input : '))
        break
    except:
        print('You can only enter number')

NameUniversity = InputUniverSity(numcount)
NameUniversity = sorted(NameUniversity,key = lambda x: (x['lenght'],['Upper']),reverse=True)

for show in NameUniversity :
    print(show.get('Upper'))

