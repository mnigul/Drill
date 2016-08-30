# -*- coding: utf-8 -*-

failiNimi = "drill.ngc"
uusFail = "drillUus.ngc"

#korjab ridadest vastavad tekstid
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

#leiab unikaalsete x loendi (leiab ainult eri x-koordinaatide arvud, korduvaid ei loe)
def leiabxUnique(x):
    xUnique = []
    for px in x:
        if not px in xUnique:
             xUnique.append(px)
    return xUnique

#parsib punktiderea punktideks
def punktiridaPunktideks(punktid, too):
    xyText = punktid[too].split('\n')
    x = []
    xy = []
    for i in range (0,len(xyText)-1):
        x.append(xyText[i].split(' ')[0])
        xy.append(xyText[i].split(' '))
    return xy, leiabxUnique(x)
    
#muudab tagasi/tagasi järjestuse tagasi/edasi 
def sorteerija(xUnique, xy):
    xyUus = []
    for i in range(0,len(xUnique)):
        pp = [k for k in xy if xUnique[i] in k]
        if i % 2 > 0:
            pp.sort()
        for pxy in pp:
            xyUus.append(pxy)	
    return xyUus

def punktideKorrigeerimine(punktid):
    punktidUus = []
    for i in range (0,len(punktid)):
        xy = []
        xyUus = []
        xUnique = []
        [xy, xUnique] = punktiridaPunktideks(punktid, i)
        xyUus = sorteerija(xUnique, xy)
        punktidUus.append(liidabPunktid(xyUus))
    punktidUus.append(" ")
    return(punktidUus)   

#Liidab punktid tagasi stringiks
def liidabPunktid(xyUus):
    punktUus = ""
    for i in range(0,len(xyUus)):
        punktUus = punktUus + xyUus[i][0] + " " + xyUus[i][1] + '\n'
    return punktUus

#kustutab tulemuse faili tyhjaks ja kirjutab uue tulemuse faili 
def failiKirjutamine(tekstid, punktid, failiNimi):
    f = open(failiNimi, 'w')
    for i in range (0, len(punktid)):
        f.write(tekstid[i]+punktid[i])
    f.write(tekstid[-1])
    f.close
          
[tekstid, punktid] = failistLugemine(failiNimi)
uusPunktid = punktideKorrigeerimine(punktid)
failiKirjutamine(tekstid, uusPunktid, uusFail)

