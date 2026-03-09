def ls_txt(a):
    o="letters used -- "
    for _ in a:
        o+=f"{_} "
    return (o)

import random
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC

ls_wr=['jazz', 'buzz', 'jazzed', 'jazzy', 'buzzed', 'jazzing', 'fizz', 'fuzz', 'buzzing', 'jinx', 'fuzzy', 'puff', 'quiz', 'fizzy', 'dizzy', 'buff', 'buzzer', 'junk', 'fizzed']
i=random.choice(ls_wr)

miss=0
guessed=[]
turns=0

while miss<7:
    output=""
    bkgrd=cv2.imread(f"hangman{miss}.png")
    bkgrd= cv2.resize(bkgrd, (1600,900))
    #screen=bkgrd.copy()
    left=0
    for w in i:
        if w in guessed:
            output+=(f"{w} ")
        else:
            output+="_ "
            left+=1
    if left==0:
        break 
    
    cv2.putText(bkgrd,output,(400,700),font,3,(255,255,0),3)
    cv2.putText(bkgrd,ls_txt(guessed),(200,200),font,1,(0,0,0),2)
    cv2.imshow("Hangman (found)",bkgrd)

    x=(cv2.waitKey(0))
    if x==27:
        break
    x=chr(x)
    if x in guessed:
        continue

    guessed.append(x)

    if x not in i:
        miss=miss+1

    turns=turns+1
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
if left==0:
    bkgrd=cv2.imread("hangman0.png")
    bkgrd= cv2.resize(bkgrd, (1600,900))
    cv2.putText(bkgrd,(f"congrats!! you finally got to {i} after {turns} turns"),(20,450),font,2,(255,255,0),3)
    cv2.imshow("Hangman (found)",bkgrd)
    cv2.waitKey(0)
else:
    bkgrd=cv2.imread("hangman7.png")
    bkgrd= cv2.resize(bkgrd, (1600,900))
    cv2.putText(bkgrd,(f"damm!! you suck at this bro."),(20,200),font,3,(255,255,0),3)
    cv2.imshow("Hangman (found)",bkgrd)
    cv2.waitKey(0)
cv2.destroyAllWindows()

