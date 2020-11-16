import random


while True:
    N=random.randrange(10,99)
    N=str(N)
    if N[0]!=N[1]:
        break
while True:
    
    player_number=int(input("Sayi giriniz: "))
    if  player_number<10 or player_number>99:
        print("Please enter another number:")
    elif (str(player_number)[0])== (str(player_number)[1]):
        print("Please enter another number:")
    else:
        true_counter=0
        false_counter=0
        player_number=str(player_number)
        if N[0]==player_number[0]:
            true_counter+=1
        else:
            false_counter+=1
        if N[1]==player_number[1]:
            true_counter+=1
        else:
            false_counter+=1
    
        print(true_counter ," ", false_counter)

        if true_counter==2:
            print("Congrats!.")
            break
        else:
            print("Please try again.")
            
     
     
    
    


     
