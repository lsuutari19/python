import haravasto as ha
import random as rd
import time
import copy
import csv
import datetime
import webbrowser

kentanmitta = {
    "leveys": 0,
    "korkeus": 0
}


lista = {
    "kenttä": [],
    "tyhjäkenttä": [],
}

tulokset = {
    "aika": 0,
    "aikaloppu": 0,
    "klikkaukset": 0
}

maa = {
    "miinat": 0,
    "liputukset": 0
}


def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    ha.tyhjaa_ikkuna() #tyhjää ikkunan
    ha.piirra_tausta() #taustaväri
    ha.aloita_ruutujen_piirto()
    for y, ruutu in enumerate(lista["tyhjäkenttä"]):
        y_koord = y * 40
        for x, avain in enumerate(ruutu):
            x_koord = x * 40
            if avain == "avattu": #tulvatäyttö
                ha.lisaa_piirrettava_ruutu("0", x_koord, y_koord)
            else:
                ha.lisaa_piirrettava_ruutu(avain, x_koord, y_koord)

    ha.piirra_ruudut()



def miinoita(kentta, jaljella, n):
    """
    Asettaa kentälle N kpl miinoja satunnaisiin paikkoihin. Miinojen määrä määritellään kysykenttä funktiossa
    """
    miina = 0
    while n > miina:
        valittu = rd.choice(jaljella)
        jaljella.remove(valittu)
        valittu_x, valittu_y = valittu
        kentta[valittu_y][valittu_x] = "x"
        miina += 1
        maa["miinat"] = miina




def laske_miinat(room):
    """
    laskee miinat tulvatäyttöä varten
    """
    miinalkm = 0
    for y, r in enumerate(room): 
        for x, p in enumerate(r): 
            if p == "x":
                continue
            if p == " ":
                miinalkm = 0
                for i in range(y - 1, y + 2):
                    if i < 0 or i >= len(room):
                        continue
                    else:
                        for j in range(x - 1, x + 2):
                            if j < 0 or j >= len(room[i]):
                                continue
                            else:
                                if room[i][j] == "x":
                                    miinalkm += 1
                room[y][x] = str(miinalkm)






def luo_kentta(leveys, korkeus):
    """
    luo kentän annettujen parametrien leveys ja korkeus perusteella
    """
    kentta = lista["tyhjäkenttä"]
    for y in range(korkeus):
        kentta.append([])
        for x in range(leveys):
            kentta[-1].append(" ")
    lista["kenttä"] = copy.deepcopy(lista["tyhjäkenttä"])
    jaljella = []
    for x in range(leveys):
        for y in range(korkeus):
            jaljella.append((x, y))
    return kentta, jaljella





def tulvataytto(alx, aly): # kysy kumpaa listaa käyttää 
    """
    Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """

    koordparilista = [(alx, aly)] #luodaan koordinaattiparilista

    while koordparilista: #lista on True niin kauan kuin siinä on arvoja joita tarkastella!

        x_koord, y_koord = koordparilista.pop() #poistaa tässä tapauksessa listasta arvon järkevämmin kuin.remove! ja lisää sen muuttujaan jota tutkitaan
        lista["tyhjäkenttä"][y_koord][x_koord] = 'avattu'
        lista["kenttä"][y_koord][x_koord] = 'avattu'

        for yk in range(y_koord - 1, y_koord + 2): #sijoittaa silmukkamuuttujiin yk ja xn mahdolliset koordinaatit
            for xn in range(x_koord - 1, x_koord + 2): 
                if (yk >= 0 and yk <= len(lista["kenttä"]) - 1) and (xn >= 0 and xn <= len(lista["kenttä"][yk]) - 1):

                    if lista["kenttä"][yk][xn] == '0':
                        koordparilista.append((xn, yk))

                    elif lista["kenttä"][yk][xn] == 'avattu':
                        continue
                    elif lista["kenttä"][yk][xn] == "1":
                        lista["tyhjäkenttä"][yk][xn] = lista["kenttä"][yk][xn]
                    elif lista["kenttä"][yk][xn] == "2":
                        lista["tyhjäkenttä"][yk][xn] = lista["kenttä"][yk][xn]
                    elif lista["kenttä"][yk][xn] == "3":
                        lista["tyhjäkenttä"][yk][xn] = lista["kenttä"][yk][xn]
                    elif lista["kenttä"][yk][xn] == "4":
                        lista["tyhjäkenttä"][yk][xn] = lista["kenttä"][yk][xn]
                    elif lista["kenttä"][yk][xn] == "5":
                        lista["tyhjäkenttä"][yk][xn] = lista["kenttä"][yk][xn]
                    
                    elif lista["kenttä"][yk][xn] == 'x':
                        lista["tyhjäkenttä"][yk][xn] = lista["kenttä"][yk][xn]






def hiiri_kasittelija(x, y, nappi, muokkausnapit):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    """
    hiiri = {
    ha.HIIRI_VASEN: "vasen",
    ha.HIIRI_KESKI: "keski",
    ha.HIIRI_OIKEA: "oikea"
    }
    x = int(x / 40)
    y = int(y / 40)
    if nappi == ha.HIIRI_OIKEA:
        tulokset["klikkaukset"] += 1
        maa["liputukset"]
        liputus(x, y)
        kentta = lista["kenttä"]
        if kentta[y][x] == "x":
            maa["miinat"] -= 1
            print(maa["miinat"])
        voittoehto()


    elif nappi == ha.HIIRI_VASEN:
        tulokset["klikkaukset"] += 1
        print(tulokset["klikkaukset"])
        avaaruutu(x, y)



def avaaruutu(x, y):
    '''avaa ruudun hiiren vasemmalla klikattaessa'''
    lista["tyhjäkenttä"][y][x] = lista["kenttä"][y][x]

    if lista["tyhjäkenttä"][y][x] == '0':
        tulvataytto(x, y)
        piirra_kentta()

    elif lista["tyhjäkenttä"][y][x] == 'x':
        tulokset["aikaloppu"] = int(time.time())  #aika pelin lopussa since 1970
        loppuaikaa = tulokset["aikaloppu"] - tulokset["aika"]
        kliks = tulokset["klikkaukset"]
        print("klikkauksia: ",kliks , "kulunut aika: ", loppuaikaa, "sekunttia")
        tuloksenotto()
        

        print("You've been gnoooomed.")
        print("         / \      ggggggggg    nnnn     nn    00000000   mmm     mmmmm  eeeeeee   ddddddd                     ")
        print("        /   \     gg           nn nn    nn   00      00  mm mm   mm mm  ee        dd     dd                   ")
        print("       /     \    gg  gggggg   nn  nn   nn   00      00  mm  mm mm  mm  eeeeeee   dd       dd                 ")
        print("      /_______\   gg  gg  gg   nn   nn  nn   00      00  mm   mm    mm  ee        dd       dd                 ")     
        print("      // . . \\    gg      gg   nn    nn nn   00      00  mm         mm  ee        dd     dd                  ")
        print("     (/(_____)\)  gggggggggg   nn     nn      0000000    mm         mm  eeeeeeee  ddddddd                     ")  
        print("     |'-' = `-'|                                                                                              ")
        print("     |         |   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                   ")
        print("     /\       /\                                                                                              ")   
        print("    /  '.   .'  \                                                                                             ") 
        piirra_kentta()
        webbrowser.open("https://www.youtube.com/watch?v=1LOD8ma2q6U&feature=youtu.be")
        ha.lopeta()

    elif lista["tyhjäkenttä"] == 'f':
        pass




def liputus(x, y):
    '''liputtaa ruudun hiiren oikealla klikattaessa'''

    if lista["tyhjäkenttä"][y][x] == ' ':
        lista["tyhjäkenttä"][y][x] = 'f'

    elif lista["tyhjäkenttä"][y][x] == 'f':
        tulokset["klikkaukset"] += 1
        maa["liputukset"] -= 1
        lista["tyhjäkenttä"][y][x] = ' '


    elif lista["tyhjäkenttä"][y][x] == 'x':
        lista["tyhjäkenttä"][y][x] = 'f'



        
    

def kysykentta():
    '''määrittää kentän dimenosion'''
    while True: #while looppi joka kysyy kentän dimensiota niin kauan että se on ideaali.
        try:
            leveys = int(input("Anna kentän leveys(min 5): "))  #kysyy kentän leveyttä
            korkeus = int(input("Anna kentän korkeus(min 5): "))  #kysyy kentän korkeutta
            miinat = int(input("Anna miinojen lkm (min 1): "))
            if leveys < 5 or korkeus < 5 or miinat <= 0:
                print("Kentän pitää olla vähintään 5 x 5 ja miinoja 1.")
            else:
                kentanmitta["leveys"] = leveys
                kentanmitta["korkeus"] = korkeus
                return leveys, korkeus, miinat                
        except ValueError:
            print("Tämä ei ole luku!")
        else:
            return leveys, korkeus, miinat



def voittoehto():
    if maa["liputukset"] == maa["miinat"]:
        if maa["miinat"] == 0:
            voittoaika = time.time()
            kliks = tulokset["klikkaukset"]
            tuloksenotto()
            laika = int(voittoaika - tulokset["aika"])
            print("klikkauksia: ",kliks , "kulunut aika: ", laika, "sekunttia")
            print("Pelastit maailman maahisilta! Hyvää työtä XD:DDD8D litfam")  
            webbrowser.open("https://www.youtube.com/watch?v=dCxb9MaI5sA&feature=youtu.be")
          
        else:
            pass



def tuloksenotto():
    """
    lisää tulokset tekstitiedostoon
    """
    tulos = tulokset["aikaloppu"] - tulokset["aika"]
    klik = tulokset["klikkaukset"]
    lev = kentanmitta["leveys"]
    kor = kentanmitta["korkeus"]
    pvm = datetime.datetime.now().strftime("%d.%m.%y klo: %H:%M:%S")
    try:
        with open("tulostiedosto.txt", 'a') as append_file:
            append_file.write("\n klikkaukset:{k}, aika:{t} sekunttia, pvm: {d} kentan koko {le}x{ko}".format(k = klik , t = tulos, d = pvm, le = lev, ko = kor))
    except IOError:
        print("Tiedostoa ei löytynyt.")


def nayta_tulokset():
    with open("tulostiedosto.txt", 'r') as read_file:
        for rivi in read_file.readlines():
            print(rivi)
    





def main():


    print("TÄMÄ ON MAAHISHARAVA!!!")
    print("Valinnat:")
    print("Aloita = a")
    print("Lopeta = l")
    print("Tulokset = t")


    valintaa = input("Tee valintasi: ")

    if valintaa == "a" or valintaa == "A":
        leveys, korkeus, miinat = kysykentta()
        lista["tyhjäkenttä"], jaljella = luo_kentta(leveys, korkeus)
        miinoita(lista["kenttä"], jaljella, miinat)
        maa["miinat"] = miinat
        laske_miinat(lista["kenttä"])
        ha.lataa_kuvat('spritet')
        ha.luo_ikkuna(len(lista["tyhjäkenttä"] * 40), len(lista["tyhjäkenttä"] * 40))
        ha.aseta_piirto_kasittelija(piirra_kentta)
        ha.aseta_hiiri_kasittelija(hiiri_kasittelija)
        tulokset["aika"] = int(time.time()) #aloittaa ajanoton 1970 luvulta :--D
        tulokset["klikkaukset"] = 0
        ha.aloita()
        
    elif valintaa == "t" or valintaa == "T":
        nayta_tulokset()
        valint = input("Paina t palataksesi päävalikkoon: ")
        if valint == "t" or "T":
            main()
        else:
            pass

    elif valintaa == "l" or valintaa == "L":
        ha.lopeta

    else:
        print("Tämä ei ole valinta.")
    

if __name__ == "__main__":
    main()




