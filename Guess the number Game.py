no = 18

print("Guess The number between 10 to 30 (you have 5 tries!!!)")


for i in range(0,5):
    a = int(input())

    if a <10 or a>30:
        print("You are guessing Out Of Range , tries left = ",4-i)
    elif a == 18:
        print('Congratulations!!! The guessed number is correct i.e. 18')
        print('You completed the game in ',i+1 ,'(try/tries)')
        break
    elif a<18:
        print('You are guessing too Low, tries left = ',4-i)
    elif a>18:
        print('you are guessing too high tries left = ',4-i)

if a !=18:
    print("GAME OVER  :-( , better luck next time")