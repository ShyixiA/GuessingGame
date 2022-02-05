from ast import Break
import random

rastgeleSayi = random.randint(1, 50)

tahminSayi = 0

while True:

    sayi=int(input("guess the number between 1 and 50 (0 EXİT):"))

    tahminSayi += 1


    if tahminSayi==10:
      print("You have no rights :(" "")
      print("Number Retained", rastgeleSayi)
      break  
    
  
    elif(sayi == 0):
        print("You Exited the Game.")
        break
 
  
  
    elif sayi < rastgeleSayi:
        print("Enter a Larger Number.")
        continue

    elif sayi > rastgeleSayi:
        print("Enter a Smaller Number.")
        continue
    

    else:
        print("Congratulations You Guessed The Number! random number = {0}".format(
            rastgeleSayi))

        print("{0} You Guessed the Number at Once.".format(tahminSayi))
        
        sayi1=int(input("press 1 to play again : "))
        sayi1 == 1   
        print("---------------------------NEW GAME---------------------------"),

