import random

ls_wr=['jazz', 'buzz', 'jazzed', 'jazzy', 'buzzed', 'jazzing', 'fizz', 'fuzz', 'buzzing', 'jinx', 'fuzzy', 'puff', 'quiz', 'fizzy', 'dizzy', 'buff', 'buzzer', 'junk', 'fizzed']

i=random.choice(ls_wr)
print(i)

miss=0
guessed=[]
turns=0
while miss<7:
    left=0
    for w in i:
        if w in guessed:
            print (f"{w} ",end="")
        else:
            print("_ ",end="")
            left=left+1

    if left==0:
        break 

    x=input("    guess:")
    
    if x in guessed:
        print("you got short term memory loss or something?")
        continue

    guessed.append(x)

    if x not in i:
        miss=miss+1

    print(f"you have got {7-miss} turns left")
    print (f"you have used {guessed}\n")
    turns=turns+1

if left==0:
    print(f"\ncongrats!! you finally got to {i} after {turns} turns")
else:
    print(f"\ndamm!! you suck at this bro.")
    
