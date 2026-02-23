import random
print("-----------------------------------------------")
print("Stone Paper Scissor Game :-")
print("-----------------------------------------------")
print("1.Stone \n2.Paper \n3.Scissor \n4.Quit game")
u=0
dict = {1:"stone",2:"paper",3:"scissor"}

while True:
    print("-----------------------------------------------")
    u = int(input("Enter Your Choice: "))
    if u==4:
        print("Thank U :)")
        break
    if u not in dict:
        print("Invalid choice !")
        continue
    c = random.randint(1,3)
    print(f"User     : {dict[u]}")
    print(f"Computer : {dict[c]}")
    if(u==c):
        print("Result   : TIE")
    elif(u==1 and c==3) or (u==2 and c==1) or (u==3 and c==2):
        print("Result   : YOU WIN !!")
    else:
        print("Result   : YOU LOSE ")

