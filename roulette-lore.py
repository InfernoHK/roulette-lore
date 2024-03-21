import random
import math
def intro():
    print("One morning you decide you want to gamble your life away (worth 50 dollars)")
    print("You go to the front desk of columbian casino and the clerk asks you to sign in with your name and age")
    name = input("By the way what is your name? ")
    print(name,"okay you are all signed in with your money which is $50 and we currently only have roulette right now")
    playq =input("Is that all right? ")
    if playq == "yes" or playq == "Yes" or playq == "yeah" or playq == "Yeah" or playq == "yup" or playq == "okay" or playq == "Okay":
        print("The clerk walks you over to the roulette table and the dealer (whos name is tyrone not important) asks you")
    else:
        print("oh all right then")
        print("*you walk out the casino*")
        exit()


    
intro()


choice = input("Do you Want to Play? ")
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
    

    if moneytotal == 0:
        loanask = input("Do you need a loan, The Dealer asks, it will cost you (%15 intrest every play) ")
        if loanask == "Yes" or loanask == "yes":
            loanmoney = int(input("how much? asks the dealer (limit of $250)"))
            loanmoney = loanmoney
            if loanmoney not in range(0,251):
                print("You have been banned from columbian casino (odered from dealer so haha)")
                exit()

            
            moneytotal = moneytotal + loanmoney



    if moneytotal > 0:
        if choice == "yes" or choice == "Yes" or choice == "yeah" or choice == "Yeah" or choice == "yup" or choice == "okay" or choice == "Okay":
            betchoice = input("Do you want to bet color and number(1) or just color(2) ")
            moneynum = int(input("How much do you want to bet? "))
            if moneynum not in range (0,moneytotal+1):
                choice = input("you dont have that money we both know that try again? (yes or no)")
                generatednum, generatedcolor = generate()
                system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice)

            moneytotal = moneytotal - moneynum
       

            if betchoice == "1" or betchoice == "color and number":
                playernum = int(input("Choose a Number Between 1 and 36 "))
                playercolor = (input("Choose a color Black or Red "))
                if playernum == generatednum and playercolor == generatedcolor:
                    print("you win")
                    print("it was", generatednum,generatedcolor)
                    moneytotal = moneytotal + 2*moneynum
                    print("your new total is", moneytotal)
                    print("$",moneytotal)

                if playercolor == generatedcolor:
                    moneytotal = moneytotal + moneynum/2
                    print("you only got the color right")
                    print("it was", generatednum,generatedcolor)
                    print("your new total is","$", moneytotal)
                else:
                    print("you lose")
                    print("it was" ,generatednum,generatedcolor)
                    print("your new total is","$", moneytotal)

            if betchoice == "2" or betchoice == "just color":
                playercolor = (input("Choose a color Black or Red"))
                if playercolor == generatedcolor:
                    moneytotal = moneytotal + 1.5*moneynum
                    print("you got it right")
                    print("it was" ,generatedcolor)
                    print("your new total is","$", moneytotal)
                else:
                    print("you got it wrong")
                    print("it was" ,generatedcolor)
                    print("your new total is","$", moneytotal)

            if loanmoney > 0:
                loanmoney = loanmoney + .15*loanmoney
                print("your loan payment is now $",loanmoney)
                loanpay = input("Make loan payment?")
                if loanpay =="yes" or loanpay == "Yes" or loanpay == "yeah" or loanpay == "Yeah" or loanpay == "yup" or loanpay == "okay" or loanpay == "Okay":
                    loanpayask = int(input("How much"))
                if loanpayask not in range(0,totalmoney+1):
                    print("You have been banned from columbian casino (odered from dealer so haha)")
                    exit()
                loanpayask = loanpayask
                totalmoney = totalmoney - loanpayask
                print("your new total is $",totalmoney,"and you still owe $", loanmoney)


            choice = input("Do you want to keep playing? ")
            while choice == "yes" or choice == "Yes" or choice == "yeah" or choice == "Yeah" or choice == "yup" or choice == "okay" or choice == "Okay":
                generatednum, generatedcolor = generate()
                system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice)
            else:
                print("Thank you for playing")
                print("*you left the casino with*","$", moneytotal)
                
        else:
            print("Loser")
            exit()
        
    

    else:
        print("you have been kicked out from the casino for trying to play without money.")
        exit()
        
generatednum, generatedcolor = generate()
system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice)