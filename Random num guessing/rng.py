import random
pwc = None
number = random.randint(1,100)
attempt = 0
def get_guess(number, attempt):
    while True:
        try:
            guess = int(input("Enter a number:"))
            attempt = attempt + 1
            wc = abs(number - guess)
            print(f"attempt no {attempt}")
            return guess, wc, attempt
        except:
            print("Please enter a valid number")
def comp(wc,pwc):
    if pwc is not None:
        if wc<pwc:
            print("Warmer!")
        elif wc>pwc:
            print("Colder!!")
        else:
            print("Same temp!!")
    pwc = wc
    return pwc
def checkwin(guess,number,attempt):
    if guess == number:
        print(f"You guessed correct!!! in {attempt} attempts")
        return True

while True:
    guess, wc, attempt = get_guess(number, attempt)
    if checkwin(guess, number,attempt):
        break
    pwc = comp(wc, pwc)
    
