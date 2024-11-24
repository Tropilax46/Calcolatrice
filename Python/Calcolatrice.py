import time
from math import *

User = input("Come ti chiami?\n")
Unit = input("Con cosa vuoi giocare?\n")

def restart():
    ask=input("Devi fare altri calcoli?\nRispondi con 'S' sennò premi qualsiasi altro pulsante\n")
    if ask.lower() != str("s"):
        return False
    else:
        return True

print(f"ciao {str(User)}!\nbenvenuto nella calcolatrice più simpatica del mondo. hihihih\noggi mi sa che giochiamo insieme con la matematica\n")

x = True
while x:
    funz = float(input("cosa ti va di utilizzare?\n\nDIGITA:\n\n1 per ADDIZIONE\n2 per SOTTRAZIONE\n3 per MOLTIPLICAZIONE\n4 per DIVISIONE\n"))
    if funz == 1:
        sumx = float(input("\nDimmi il primo numero che vuoi sommare!\n"))
        sumy = float(input("\nPerfetto, adesso dimmi il secondo numero che vuoi sommare!\n"))
        sumresult = sumx + sumy
        print(f"\nLa somma fra {str(sumx)} e {str(sumy)} è:\n{str(sumresult)} {str(Unit)}\n")
        time.sleep(2)
    elif funz == 2:
        subx = float(input("\nDimmi il primo numero che vuoi sottrarre!\n"))
        suby = float(input("\nPerfetto, adesso dimmi il secondo numero che vuoi sottrarre!\n"))
        subresult = subx - suby
        print(f"\nLa sottrazione fra {str(subx)} e {str(suby)} è:\n{str(subresult)} {str(Unit)}\n")
        time.sleep(2)
    elif funz == 3:
        mulx = float(input("\nDimmi il primo numero che vuoi moltiplicare!\n"))
        muly = float(input("\nPerfetto, adesso dimmi il secondo numero che vuoi moltiplicare!\n"))
        mulresult = mulx * muly
        print(f"\nLa moltiplicazione fra {str(mulx)} e {str(muly)} è:\n{str(mulresult)} {str(Unit)}\n")
        time.sleep(2)
    elif funz == 4:
        divx = float(input("\nDimmi il primo numero che vuoi dividere!\n"))
        divy = float(input("\nPerfetto, adesso dimmi il secondo numero che vuoi dividere!\n"))
        if divy!=0:
            divresult = divx / divy
            print(f"\nLa divisione fra {str(divx)} e {str(divy)} è:\n{str(divresult)} {str(Unit)}\n")
            time.sleep(2)
        else:
            print("\nNon si può dividere per 0\n")
            time.sleep(2)
    else:
        print("\nERRORE\nHai inserito qualcosa di sbagliato :P\nRiprova ;D\n")
        time.sleep(2)
        continue

    x = restart()
    continue

exit = input(f"\nGrazie {str(User)} per aver giocato insieme a me!\nCi vediamo, alla prossima.\n\nPremi invio per uscire")