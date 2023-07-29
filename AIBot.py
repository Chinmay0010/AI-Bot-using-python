#My_Bot
import time
import random
def _init_(self,user_name,password):
    self.user_name = user_name
    self.password = password
def info(self):
    return f"User_Name-{self.user_name}\nPassword-{self.password}"

start = print("Hey! I am your bot")
time.sleep(2)
ask_name = print("Btw whos this?")

Name = input("Like you tell me your name: ")
time.sleep(1)

greeting_choice = random.choice(["Hello","Hey","Hi","Namaskar","Namaste"])
print(f"{greeting_choice} {Name}")

intro = input(f"Hey do you want to know me {Name}?: ")
intro2= intro.lower()
if intro2 == "yes":
    print(f"{greeting_choice} am 'BollyBot'\n I was created by 'Chinmay Gaikwad' in 2023\n I like humans so i like you as well. ")
    time.sleep(3)
elif intro2 == "no":
    print("Ok I guess you know me already")
    time.sleep(2)
else:
    print("That was not something I was expecting")

time.sleep(5)
compliment = random.choice(["Btw You look so good today","Btw Nice hair style","Btw I like your personality"])
print(compliment)
time.sleep(6)



play = (input("Do you want play something: "))
if play == "yes":
    print("lets play my favourite rock paper and scissors")
elif play == "no":
    print(myfucn())
        
 
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)

#RPS

player1 = input("Enter your choice: ")
player2 = random.choice(["rock","paper","scissor"])
print(player2)
if player1 == player2:
    print("its a tie")
elif player1 == "rock":
    if player2 == "scissor":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player1 == "paper":
    if player2 == "rock":
        print("Paper covers rock! You lose.")
    else:
        print("Scissors cuts paper! You lose.")
elif player1 == "Scissors":
    if player2 == "rock":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

time.sleep(3)
print(f"It was nice playing with {Name}")
time.sleep(4)

city_guess = random.choice(["mumbai","pune","delhi"])
print(f"Hey {Name} are you from {city_guess}?")
city_input = input("Are you: ")
if city_input == "yes":
    print(f"Ohh! even I am from {city_guess} We can meet someday")
elif city_input == "no":
    print("ohh sad!")
else:
    print("That was not something I was expecting!")

time.sleep(3)

yoga = print(input("Do you want to do feel relaxed?: "))
if yoga == "yes":
    print("sit back and relax and just follow my instructions")
elif yoga == "no":
    print("ok! take care honey")
    time.sleep(100)

time.sleep(3)
print("We'll do simple inhale exhale workout")
time.sleep(3)
print(f"{Name} inhale now")
time.sleep(2)

time.sleep(1)
print("Exhale now")
time.sleep(3)
print("Inhale now")
time.sleep(1)

time.sleep(2)
print("Exhale now")
time.sleep(3)
print("Inhale now")
time.sleep(1)

time.sleep(2)
print("Exhale now")      
time.sleep(2)
print("I hope you are feeling a bit relaxed")

time.sleep(3)

#ratingpanel
x = print(input(f"On the scale of 1-10 how much will you rate us : "))
if x == "5":
    print("we are trying to improve more")
elif x == "6" or x == "7" or x == "8":
    print("Thnakyou for your feedback")
elif x == "9" or x == "10":
    print("I know you love me now!")
else:
    print("Thnakyou for your feedback\nI know you love me now")