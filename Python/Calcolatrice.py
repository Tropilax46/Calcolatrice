print("ciao bello!\nbenvenuto nella calcolatrice più simpatica del mondo. hihihih\noggi mi sa che giochiamo insieme con la matematica\n")
x = True
while x == True:
    funz = input ("cosa ti va di utilizzare?\n\nDIGITA:\n\n1 per ADDIZIONE\n2 per SOTTRAZIONE\n3 per MOLTIPLICAZIONE\n4 per DIVISIONE\n")
    if funz == 1:
        sumx = input ("Dimmi il primo numero che vuoi sommare!\n")
        sumy = input ("perfetto, adesso dimmi il secondo numero che vuoi sommare!\n")
        sumresult = sumx + sumy
        print("la somma fra " + str(sumx) + "e" + str(sumy) + "è" + str(sumresult) + "\n")
        continue
    elif funz == 2:
        subx = input ("Dimmi il primo numero che vuoi sottrarre!\n")
        suby = input ("perfetto, adesso dimmi il secondo numero che vuoi sottrarre!\n")
        subresult = subx + suby
        print("la sottrazione fra " + str(subx) + "e" + str(suby) + "è" + str(subresult) + "\n")