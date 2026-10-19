import random

name = input("Hi! I'm Chatbot. What's your name? ")
print(f"Hey! {name}, nice to meet you.")

# GOOD/BAD
a = input('How are you today? (good/bad) ')

if a == 'good':
    print("I see, That's lovely to hear!")
elif a == 'bad':
    print("Oh, don't worry we all have bad days, things will be better soon!")
else:
    print("No worries, it can be hard to put your feeling into words at times.")
# GOOD/BAD

# HOBBY
hobby = input(f"By the way {name}, what is your hobby? ")
print(f"Oh! {hobby} sounds very fun! My hobby is learning new things!")
#HOBBY

#GAME
ans = input(f"Say, {name}, are you up for a guessing game? (yes/no) ")

if ans.lower() == "yes":
    num = random.randint(1,100)
    print("Guess the random number I chose! (from 1 to 100)")
    while True:
        guess = int(input("Guess: "))
        if guess > num:
            print("Lower!")
        elif guess < num:
            print("Higher!")
        elif guess == num:
            print(f"Well done {name}!")
            break
#GAME       

print("I had a great time chatting with you, let's talk again sometime!")