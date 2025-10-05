
secret_number = 7


guess = 0 
attempts = 0

print("Welcome to the Random Guessing Game!")
print("I'm thinking of a number between 1 and 10.")


while guess != secret_number:
    attempts += 1
    
    
    inputnum = input(f"Attempt #{attempts}: Type your guess (1 to 10): ")
    guess = int(inputnum)
    
    
    if guess < 1 or guess > 10:
        print("Stay between 1 and 10")
    elif guess < secret_number:
        print("Too low! Try again")
    elif guess > secret_number:
        print("Too high!")
    

print(f" WOOHOO!")
print(f"The secret number was indeed #{secret_number}.")

if attempts == 1:
    print("FIRST TRY?! You're a legend!")
elif attempts <= 3:
    print(f"Only {attempts} attempts! That's excellent work.")
else:
    print(f"After {attempts} tries, you finally got it.")