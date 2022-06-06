import random


print("Welcome to Rock, Paper, Scissors GAME: The Game will be Played with COMPUTER\n\n")
print("Winning Rules of the Rock paper scissor game are: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
print("Player Options are: \n"
                            +'"R" for "rock",\n' 
                            +'"P" for "paper",\n' 
                            +'"S" for "scissors"\n')
is_runing=True
while is_runing:
         
    def PHand():   
        store = ["R","P","S"]
        Player=input("Player your Hand: ").upper()
        while Player not in store:
            Player=input("Player your Hand: ").upper()
            print("invalid Input, Please refer to instructions")
        if Player in store:
            return Player 
        return Player
    def Computer():
        store = ["R","P","S"]
        CPU= random.choice(store)
        return CPU
    CPU=Computer()
    PHand=PHand()  
    if CPU=="S":
        CPU="Scissors"
    elif CPU=="R":
        CPU="Rock"
    else:
        CPU="Paper" 
    if PHand=="S":
        PHand="Scissors"
    elif PHand=="P":
        PHand="Paper"
    else:
        PHand="Rock"    

    print("Player({})".format(PHand)+":CPU({})".format(CPU))

    if CPU=="Rock" and PHand=="Scissors":
        print("Computer Wins")
        is_runing=False
    elif CPU=="Scissors" and PHand=="Rock":
        print("Player wins")
        is_runing=False
    elif CPU=="Paper" and PHand=="Rock":
        print("Computer wins")
        is_runing=False
    elif CPU=="Rock" and PHand=="Paper":
        print("Player wins")
        is_runing=False
    elif CPU=="Scissors" and PHand=="Paper":
        print("Computer win")
        is_runing=False
    elif CPU=="Paper" and PHand=="Scissors":
        print("Player wins")
        is_runing=False
    else:
        is_runing=True
        
        
    
    
    

