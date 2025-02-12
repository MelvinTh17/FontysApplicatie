from datetime import datetime
 
def check_kenteken():
    kentekens = ["SZ-800-S", "89-XTX-1", "VRG-81-T", "VPS-23-V", "VRS-36-J"]
    kenteken = input("Wat is je kenteken?")
    if kenteken in kentekens:
      bepaal_tijd()
    else:
      print("U heeft helaas geen toegang tot het parkeerterrein")
    


def bepaal_tijd():
    nu = datetime.now()
    uur = nu.hour
    if(uur > 23 or uur < 7):
      print("Sorry, de parkeerplaats is ’s nachts gesloten")
    else:
        groet = bepaal_bericht(uur)
        print(groet + " Welkom bij Fonteyn Vakantieparken")
 
def bepaal_bericht(uur):
    if 7 <= uur < 12:
        return "goedemorgen!"
    elif 12 <= uur < 18:
        return "goedemiddag!"
    elif 18 <= uur < 23:
        return "goedenavond!"
 
 
if __name__ == "__main__":
    check_kenteken()