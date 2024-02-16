liste=[pow(2,p) for p in range(0,64)]
print(liste)
ruselt=[]
liste_element=[3,5,4,7,10,12]
for i in liste_element:
    for j in liste:
        if i+j in liste_element:
            ruselt.append(i)
            ruselt.append(j+i)
print(ruselt)