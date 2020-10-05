import random


print(" Welcome to the dice game ")

y=input(" enter \"yes\" to play the game ")

while (y=="yes") :
    c=random.randint(1,6)
    if c==1 :
        print(" ""-"*6)
        print(" |         |")
        print(" |    *    |")
        print(" |         |\n","- "*6)
    elif c==2 :
        print(" ""-" * 6)
        print(" |         |")
        print(" | *    *  |")
        print(" |         |\n","- " * 6)
    elif c==3 :
        print(" ""-" * 6)
        print(" |    *    |")
        print(" |    *    |")
        print(" |    *    |\n","- " * 6)

    elif c==4 :
        print(" ""-" * 6)
        print(" |  *    * |")
        print(" |         |")
        print(" |  *    * |\n","- " * 6)

    elif c==5 :
        print(" ""-" * 6)
        print(" |  *    * |")
        print(" |     *   |")
        print(" |  *    * |\n","- " * 6)

    else:
        print(" ""-" * 6)
        print(" |  *    * |")
        print(" |  *    * |")
        print(" |  *    * |\n","- " * 6)

    y=input(" if you want to play again then press \"yes\" ")





















