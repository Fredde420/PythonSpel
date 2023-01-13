import random as rand
import time
import sys

def clear():
    clear = "\n" * 100
    time.sleep(1)
    print(clear)

def skriv_ut(stringtoprint):
    for i in stringtoprint:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

def start():
    skriv_ut(
    """
    Välkommen till mulle mecks äventyrsspel, du befinner dig i kylarköping.
    Detta spel går ut på att komma upp i en sådan hög level som möjligt!
    Du kommer slåss mot olika innvånare i byn och ställa dina sten, sax och påse kunskaper på prov!
    Du kommer presenteras med tre dörrar som antingen har en invånre, en kista med godsaker eller en fälla!
    Men först ska du bygga din karaktär.
    """)

def menu():
    gåvidare = int(input("vill du gå vidare, skriv 1 för Ja,  2 för Nej:  "))
    if gåvidare == 1:
        skriv_ut("går vidare......")
    elif gåvidare == 2:
        exit()
    else:
        skriv_ut("Välj mellan 1 och 2")
        clear()
        menu()


class Player:
    def karaktärbygge(self):
        self.namn = input("vad är ditt namn: ")
        self.hudfärg = input("vad är din hudfärg? ")
        self.hårfärg = input("vilken hårfärg har du: ")
        self.HP = 40
    pass

player = Player()

def karaktär():
    player.karaktärbygge()

# Modified Monster class
import random

class Monster:
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def __str__(self):
        return f"{self.name}"

# List of possible names for the monster
namn = ["Sally", "Bärgarn", "Rödis", "Guido", "Chick Hicks", "Luigi", "Mack"]

# Väljer någon av namnen från listan, 
namn_index = random.randint(0, len(namn) - 1)
valt_namn = namn[namn_index]

# Monster med något av namnen
monster = Monster(valt_namn, 30)


def val():
    clear()
    while True:
        alt = int(input(
            """
            vill du gå vidare till dörrarna tryck 1
            Eller vill du kolla din ryggsäck tryck 2 
            Eller kolla din lv och hp tryck 3
            eller tryck 4 för avsluta
            """))
        if alt == 1:
            dörrar()

        elif alt == 2:
            print("ryggskäck")
        elif alt == 3:
            skriv_ut(str(player.HP))

        elif alt == 4:
           exit()  
        else:
            skriv_ut("{player.namn}, vvälj ett nummer mellan 1 och 3")
            val()
            
 
def dörrar():
    print(
    """
    Vad vill du göra?
   1. dörr 1                    2. dörr 2                     3. dörr 3           
 __________________           __________________           __________________
/    __________    \         /    __________    \         /    __________    \ 
|   /          \   |         |   /          \   |         |   /          \   |
|   |          |   |         |   |          |   |         |   |          |   |
|   |          |   |         |   |          |   |         |   |          |   |
|   |          |   |         |   |          |   |         |   |          |   |
|   \__________/   |         |   \__________/   |         |   \__________/   |
|                  |         |                  |         |                  |
|    __      __    |         |    __      __    |         |    __      __    |
|   /  \    /  \   |         |   /  \    /  \   |         |   /  \    /  \   |
|   |  |    |  |   |         |   |  |    |  |   |         |   |  |    |  |   |
|   |  |    |  |   |         |   |  |    |  |   |         |   |  |    |  |   |
|   \__/    \__/   |         |   \__/    \__/   |         |   \__/    \__/   |
\__________________/         \__________________/         \__________________/
"""
    )
    lista = [1,2,3] 
    tal = rand.choice(lista)
    int(input("välj en dörr 1,2 eller 3: ")) 
    
    if tal == 1:
        player.HP = player.HP -5
        skriv_ut(f"{player.namn}, du öppnade en fälla och tappar där av 5 hp. Ditt hp är nu {player.HP} ")
        if player.HP > 0: 
          dörrar()
        else:
          skriv_ut("Du förlorade")
          sys.exit
    elif tal == 2:
        print("kista")
        dörrar()
        #kista här
    elif tal == 3:
        skriv_ut(
            """
            Mulle:
            ojojoj bakom denna dörr väntade inte en fräsig kärra,
            utan du har kommit fram till ett monster.
            Jag hoppas att du har vässat dina sten, sax och påse kunskaper
            för nu kommer de behövas!
            """
        )
        strid()

    return

def strid():
    val = input("Välj sten sax eller påse: ")
    if val == "sten":
        random_int = rand.randint(1,3)
        if random_int == 1:
          monster.HP = monster.HP-5
          skriv_ut(f"Mulle: looking good som man säger i amerikat! {monster} valde sax. Du har {player.HP} HP kvar! Monstret {monster.HP} HP kvar.\n")
          if player.HP > 0:  
                strid()
          else:
                skriv_ut("Du förlora")
                sys.exit()
        elif random_int == 2:
            player.HP = player.HP-5
            skriv_ut(f"Mulle: Denna gång lyckades du inte men ge inte upp! {monster} valde påse. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.\n")
            if player.HP > 0:  
                strid()
            else:
                skriv_ut("Du förlora")
                sys.exit()
        elif random_int == 3:
            skriv_ut(f"Mulle: slipps som man säger i amerikat (tie), {monster} valde sten. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.\n")
            if player.HP > 0:  
                strid()
            else:
                skriv_ut("Du förlora")
                sys.exit()

    if val == "sax":
        random_int = rand.randint(1,3)
        if random_int == 1:
          monster.HP = monster.HP-5
          skriv_ut(f"Mulle: looking good som man säger i amerikat! {monster} valde påse. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.\n")
          if player.HP > 0:  
                strid()
          else:
                skriv_ut("Du förlora")
                sys.exit()
        elif random_int == 2:
            player.HP = player.HP-5
            skriv_ut(f"Mulle: Denna gång lyckades du inte men ge inte upp! {monster} valde sten. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.\n")
            if player.HP > 0:  
                strid()
            else:
                skriv_ut("Du förlora")
                sys.exit()
        elif random_int == 3:
            skriv_ut(f"Mulle: slipps som man säger i amerikat (tie), {monster} valde sax. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.\n")
            if player.HP > 0:  
              strid()
            else:
                skriv_ut("Du förlora")
                exit

    if val == "påse":
          random_int = rand.randint(1,3)
          if random_int == 1:
            monster.HP = monster.HP-5
            skriv_ut(f"Mulle: looking good som man säger i amerikat! {monster} valde sten. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.\n")
            if player.HP > 0:
              strid() 
            else:
              skriv_ut("Du förlora")
              exit
          elif random_int == 2:
            player.HP = player.HP-5
            skriv_ut(f"Mulle: Denna gång lyckades du inte men ge inte upp! {monster} valde sax. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.\n")
            if player.HP > 0:  
              strid()
            else:
              skriv_ut("Du förlora")
              exit
          elif random_int == 3:
            skriv_ut(f"Mulle: slipps som man säger i amerikat (tie), {monster} valde påse. Du har {player.HP} hp kvar! Monstret {monster.HP} HP kvar.\n")
            if player.HP > 0: 
              strid()
            else:
              skriv_ut("Du förlora")
              exit



clear()
start()
clear()
karaktär()
clear()
menu()      
clear()
dörrar()
clear()