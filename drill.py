failiNimi = "drill.ngc"
uusFail = "drillUus.ngc"

#korjab ridadest  vastava tekstid
def kogumine(tekst,line):
    return tekst + line

#faili lugemine ja kaheks jagamine: tekst ja punktide koordinaadid  
def failistLugemine(failiNimi):
    tekst = ""
    punkt = ""
    tekstid = []
    punktid = []
    f = open(failiNimi, 'r')
    for line in f.readlines():
        rida = line.split(" ")
        if rida[0] == "G81":
            rida = line.split("X")
            tekst = (kogumine(tekst,rida[0]))
            tekstid.append(tekst)
            tekst = ""
            punkt = 'X' + rida[1]
        elif rida[0][0] == 'X':
            punkt = kogumine(punkt,line)
        else:
            if len(punkt)>0:
                punktid.append(punkt)
                punkt = ""
            tekst = kogumine(tekst, line) 
    tekstid.append(tekst)
    f.close
    return tekstid, punktid

#kustutab tulemuse faili tyhjaks ja kirjutab uue tulemuse faili 
def failiKirjutamine(tekstid, failiNimi):
    f = open(failiNimi, 'w')
    for i in range (0, len(punktid)):
        f.write(tekstid[i]+punktid[i])
    f.write(tekstid[-1])
    f.close
          
[tekstid, punktid] = failistLugemine(failiNimi)
uusFail = failiKirjutamine(tekstid, uusFail)
