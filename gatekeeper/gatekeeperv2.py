from datetime import datetime
 
 
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
    bepaal_tijd()
