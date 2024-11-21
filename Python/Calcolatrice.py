import time

print("ciao bello!\nbenvenuto nella calcolatrice più simpatica del mondo. hihihih\noggi mi sa che giochiamo insieme con la matematica\n")
x = True
while x:
    funz = float(input("cosa ti va di utilizzare?\n\nDIGITA:\n\n1 per ADDIZIONE\n2 per SOTTRAZIONE\n3 per MOLTIPLICAZIONE\n4 per DIVISIONE\n"))
    if funz == 1:
        sumx = float(input("Dimmi il primo numero che vuoi sommare!\n"))
        sumy = float(input("perfetto, adesso dimmi il secondo numero che vuoi sommare!\n"))
        sumresult = sumx + sumy
        print("la somma fra " + str(sumx) + " e " + str(sumy) + " è:\n" + str(sumresult) + "\n")
        time.sleep(2)
        continue
    elif funz == 2:
        subx = float(input("Dimmi il primo numero che vuoi sottrarre!\n"))
        suby = float(input("perfetto, adesso dimmi il secondo numero che vuoi sottrarre!\n"))
        subresult = subx - suby
        print("la sottrazione fra " + str(subx) + " e " + str(suby) + " è:\n" + str(subresult) + "\n")
        time.sleep(2)
        continue
    elif funz == 3:
        mulx = float(input("Dimmi il primo numero che vuoi moltiplicare!\n"))
        muly = float(input("perfetto, adesso dimmi il secondo numero che vuoi moltiplicare!\n"))
        mulresult = mulx * muly
        print("la moltiplicazione fra " + str(mulx) + " e " + str(muly) + " è:\n" + str(mulresult) + "\n")
        time.sleep(2)
        continue
    elif funz == 4:
        divx = float(input("Dimmi il primo numero che vuoi dividere!\n"))
        divy = float(input("perfetto, adesso dimmi il secondo numero che vuoi dividere!\n"))
        if divy!=0:
            print("la divisione fra " + str(divx) + " e " + str(divy) + " è:\n" + str(divresult) + "\n")
            divresult = divx / divy
            time.sleep(2)
        else:
            print("Non si può dividere per 0\n")
        time.sleep(2)
        continue
    else:
        print("ERRORE\nHai inserito qualcosa di sbagliato :P\nRiprova ;D\n")
    time.sleep(2)
    restart =input("Se devi fare altri calcoli?\nRispondi con 'S' sennò premi qualsiasi altro pulsante")
    if restart != restart.lower():
        x = False
        