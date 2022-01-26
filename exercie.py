


'''
game = (
[0,2,0],
[1,0,0],
[0,0,0]
)
player1  X  
player2  O
position = input("Enter your position: Ex L,C 1,2 ..: ").split(",")
print(position)
['1', '1']
# print(game[1][0])
print(game[int(position[0])][int(position[1])])



player1_symbol = 'X'
player2_symbol = 'O'	
print("-----------------")
print('|', )
'''
import random
nombre=int(input("donner :")) #69
liste=[]
list1=[]
z=101
x=1
for i in range(x,z):
    liste.append(i)
    list1.append(i)
retry=1
'''ordi=random.choice(list1)
list1=[]
print(ordi)
print(liste[ordi:51])
for i in liste[ordi:51]:
            list1.append(i)
print(list1)
'''
while True:
    ordi=random.choice(list1)
    #liste = list1 #23
    list1=[]

    if ordi==nombre :
        print("Vrai")
        print(ordi)
        break
    elif ordi < nombre :#123456789    ordi 5  moi 2
        print("petit")
        print(ordi)
        retry+=1

        for i in liste[ordi:z]:
            list1.append(i)
        #liste=list1
        print(list1)
        x=ordi
    else:
        print("grand")
        print(ordi)

        retry+=1
		#liste = [1,2,3,4,5] --> 
        for i in liste[x:ordi]:
            list1.append(i)
       # liste=list1
        z=ordi
        print(list1)
print("nombre de retry est :",retry)
