# chance = 1
# targetNum = 9
# guess = int(input("Guess the number: "))
# while guess != targetNum:
#     print("Wrong guess")
#     chance += 1
#     guess = int(input("Guess the number: "))
#     if chance > 3:
#         print("You failed to guess")
#         break
# print("You guessed it right")


secret_num = 9
chance = 1
while chance <= 3:
    chance += 1
    guess = int(input("Guess: "))
    if guess == secret_num:
        print("You guessed it right")
        break
else:
    print("You should guess it in 3 attemps")

