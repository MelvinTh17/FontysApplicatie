try:
 aantal = int(input("Hoe vaak wil je de loop uitvoeren?"))
except: 
 print("Vul een heel getal in!")

def tellen():
    for i in range(aantal):
      print(f"Alarm {i+1} !")
