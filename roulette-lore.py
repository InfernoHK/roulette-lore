import random
import math
def intro():
    print("One morning you decide you want to gamble your life away (worth 50 dollars)")
    print("You go to the front desk of columbian casino and the clerk asks you to sign in with your name and age")
    name = input("By the way what is your name? ")
    print(name,"okay you are all signed in with your money which is $50 and we currently only have roulette right now")
    playq =input("Is that all right? ")
    while playq not in ("yes" , "no"):
        playq = input("Enter yes or no ")
    if playq == "yes":
        print("The clerk walks you over to the roulette table and the dealer (whos name is tyrone not important) asks you")
    elif playq == "no":
        print("oh all right then")
        print("*you walk out the casino*")
        exit()
    else:
            print("Please Enter yes or no")

    


    
intro()


choice = input("Do you want to Play? ")
playernum = int()
playercolor = ("")
moneytotal = 50
moneynum = int()
betchoice = int()



def generate():
    generatednum = random.randint(1,36)
    generatedcolor = random.choice(["red", "black"])
    
    return generatednum, generatedcolor
    

def system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice):
    
    loanmoney = 0
    loanpayask = 0

    if moneytotal == 0:
    
        loanask = input("Do you need a loan, The Dealer asks, it will cost you (+ %15 intrest every round) ")
        while loanask not in ("yes","no"):
            loanask = input("Enter yes or no ")

        if loanask == "yes":
            loanmoney = int(input("how much? asks the dealer (limit of $250) "))
            loanmoney = loanmoney
    
            if loanmoney not in range(0,251):
                print("You have been banned from columbian casino (odered from dealer so haha) ")
                exit()

            
            moneytotal = moneytotal + loanmoney
        elif loanask == "no":
            print("you have been kicked out from the casino for trying to play without money. ")
            exit()




    if moneytotal > 0:
        while choice not in ("yes", "no"):
            choice = input("Enter yes or no ")
        if choice == "yes":
            betchoice = input("Do you want to bet on color and number(1) or just color(2) ")
            while betchoice not in ("1","color and number","2","just color"):
                betchoice = input("Please enter 1, 2, color and number, or just color ")
            while True:
             try:
                 moneynum = int(input("How much do you want to bet? "))
                 break
             except ValueError:
                    print("Please enter a whole number")
            
                
            
           
            
            if moneynum not in range (0,math.ceil(moneytotal+1)):
                choice = input("you dont have that money we both know that try again? (yes or no) ")
                generatednum, generatedcolor = generate()
                system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice)

            moneytotal = moneytotal - moneynum
       

       

            if betchoice == "1" or betchoice == "color and number":
                playernum = int(input("Choose a Number Between 1 and 36 "))
                while playernum not in range(1,37):
                    playernum = int(input("Please enter a valid number "))
                
                playercolor = (input("Choose a color Black or Red "))
                while playercolor not in ("black", "red"):
                    playercolor = input("Enter black or red ")
                if playernum == generatednum and playercolor == generatedcolor:
                    print("you win")
                    print("it was", generatednum,generatedcolor)
                    moneytotal = math.ceil(moneytotal + 2*moneynum)
                    print("your new total is", moneytotal)
                    print("$",moneytotal)

                if playercolor == generatedcolor:
                    moneytotal = math.floor(moneytotal + moneynum/2)
                    print("you only got the color right")
                    print("it was", generatednum,generatedcolor)
                    print("your new total is","$", moneytotal)
                else:
                    print("you lose")
                    print("it was" ,generatednum,generatedcolor)
                    print("your new total is","$", moneytotal)

            if betchoice == "2" or betchoice == "just color":
                playercolor = (input("Choose a color Black or Red "))
                while playercolor not in ("black", "red"):
                    playercolor = input("Enter black or red ")
                if playercolor == generatedcolor:
                    moneytotal = math.ceil(moneytotal + 1.5*moneynum)
                    print("you got it right")
                    print("it was" ,generatedcolor)
                    print("your new total is","$", moneytotal)
                else:
                    print("you got it wrong")
                    print("it was" ,generatedcolor)
                    print("your new total is","$", moneytotal)

            if loanmoney > 0:
                loanmoney = math.ceil(loanmoney + .15*loanmoney)
                print("your loan payment is now $",loanmoney)
                loanpay = input("Make loan payment?(you have to so) ")
                while loanpay not in ("yes", "no"):
                    loanpay = input("Enter Yes or no ")
                if loanpay =="yes":
                    loanpayask = int(input("How much "))
                if loanpayask not in range(1,math.ceil(moneytotal)):
                    print("You have been banned from columbian casino (told you)")
                    exit()
                elif loanpay == "no":
                    print("You have been banned from columbian casino (told you)")
                    exit()
                elif moneytotal == 0:
                    print("You have no money to pay off your loan you have been kicked out")
                    exit()


                loanpayask = loanpayask
                moneytotal = moneytotal - loanpayask
                print("your new total is $",moneytotal,"and you still owe $", loanmoney)



            choice = input("Do you want to keep playing? ")
            while choice not in ("yes","no"):
                choice = input("Enter yes or no ")
            if choice == "yes":
                generatednum, generatedcolor = generate()
                system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice)
            elif choice == "no" and loanmoney:
                print("Thank you for playing")
                print("*you left the casino with*","$", moneytotal)
                exit()
                
        elif choice =="no":
            print("Loser")
            exit()
        

    else:
        print("you have been kicked out from the casino for trying to play without money.")
        exit()
        
generatednum, generatedcolor = generate()
system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice)