import socket
from os import system

#Lijstje met kleurcoderingen voor weergave van poorten
class style():
  ROOD = '\033[31m'
  GROEN = '\033[32m'
  BLAUW = '\033[34m'
  RESET = '\033[0m'
  DIK = '\033[1m'

#Maak de terminal schoon
clear = lambda: system('clear') 
clear()
#Open poorten worden verzameld voor samenvatting
open_poorten = []

#Lijstjes met poorten, misschien nog mogelijkheid maken voor zelf invoeren?
veel_poorten = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 135, 137, 138, 139, 143, 161, 162, 179, 194, 443, 445, 465, 514, 515, 587, 631, 993, 995, 1433, 1434, 1521, 1723, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 9000, 9092, 9200, 11211, 27017, 50000, 50070]
weinig_poorten = [20, 21, 22, 23, 25, 53, 80, 110, 443, 445]

def verzamelgegevens():
    #INTRODUCTIE
    print(r"""

    ___  ___     _       _       
    |  \/  |    | |     (_)      
    | .  . | ___| |_   ___ _ __  
    | |\/| |/ _ \ \ \ / / | '_ \ 
    | |  | |  __/ |\ V /| | | | |
    \_|  |_/\___|_| \_/ |_|_| |_|
                                
                                


                    """)
    print(f"{style.DIK}Welkom bij de fontys poortsniffer 3000{style.RESET}")

    #Vraag om gegevens
    host = input("Vul je ip in die je graag wil sniffen:")
    lijstnr = input("Welke poorten? A. 10 meest voorkomende of B. 50 poorten?")



    if(lijstnr == "A" or lijstnr == "a"):
      iplijst = weinig_poorten
    elif(lijstnr == "B" or lijstnr == "b"):
      iplijst = veel_poorten
    else:
      print("Sorry! Je hebt volgens mij een foute reactie gegeven! A of B?")
    
    scan(iplijst, host)
    
def scan(iplijst, host):
    clear()
    print(f"bezig met scannen van {host}......")
    #Poorten checken
    for poort in iplijst:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket opzetten
            s.settimeout(2) #Wat is een goede timeout? Weet niet zeker als 2 seconden genoeg tijd geeft voor antwoord
            s.connect((host, poort)) #Zet verbinding op naar poort
            print(f"Poort {poort} is {style.GROEN}OPEN{style.RESET}") #Print open poort
            open_poorten.append(poort) #Voeg open poort toe aan lijstje
            s.close() #Sluit socket
        except socket.error: 
            print(f"Poort {poort} is {style.ROOD}GESLOTEN{style.RESET}") #Print gesloten poort
    samenvatting(iplijst)

def samenvatting(iplijst):
    ######   SAMENVATTING VAN OPEN POORTEN  ########
    print(f"{style.BLAUW}Samenvatting van open poorten{style.RESET}")
    print("------------------------------------")
    print(f"{len(open_poorten)} van de {len(iplijst)} poorten open")
    print("------------------------------------")
    for open in open_poorten:
      print(f"Poort - {style.GROEN}{open}{style.RESET}")
      print("------------------------------------")

if __name__ == "__main__":
    verzamelgegevens()
