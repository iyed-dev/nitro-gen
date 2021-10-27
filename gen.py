import random, string
import os
import time


time.sleep(1)
os.system("color c")
print("""
© Copyright Iyed Amri - All reserved
""")


time.sleep(1)
print("""
Génération de vos Discord Nitro (uncheck) en cours...
""")
time.sleep(1)
print("""
/!\ vous pouvez arrêter le logiciel quand vous voulez.
""")
print("""
Vos Discord Nitro (uncheck) seront sauvegarder dans un fichier texte !
""")

while True:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('nitro.json', "a+")
    f.write(f'{code}\n')
    f.close()