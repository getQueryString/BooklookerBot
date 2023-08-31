# Copyright© by getQueryString/Fin

import requests
import time


class BooklookerBot:
    def __init__(self, TELEGRAM_API_KEY):
        self.base_url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/"
        self.chat_id = None

    def send_get_request(self):
        while True:
            print("Anfrage gesendet.")
            request = requests.get(WEBSITE)
            if "Es wurden keine passenden Artikel gefunden." not in request.text:
                for i in range(5):
                    booklooker_bot.handle_updates(
                        f"{MESSAGE_TEMPLATE}GEFUNDEN!")
                    time.sleep(1)
                break
            else:
                booklooker_bot.handle_updates(
                    f"{MESSAGE_TEMPLATE}NOCH NICHT GEFUNDEN!")
            time.sleep(3600)  # Alle 60 Minuten

    def get_updates(self):
        url = f"{self.base_url}getUpdates?timeout=100"
        response = requests.get(url)
        return response.json()["result"]

    def send_message(self, chat_id, text):
        url = self.base_url + f'sendMessage?chat_id={chat_id}&text={text}'
        requests.get(url)

    def handle_updates(self, text):
        updates = self.get_updates()
        if updates:
            for update in updates:
                message = update["message"]
                self.chat_id = message["chat"]["id"]
            self.send_message(self.chat_id, text)


if __name__ == '__main__':
    try:
        print("Bot gestartet.\n")
        MAX_PRICE = 6
        TITLE = ""
        MESSAGE_TEMPLATE = f"Suche nach dem Buch \"{TITLE}\" für einen Maximalpreis von {MAX_PRICE} €:\n"
        TELEGRAM_API_KEY = ""
        WEBSITE = f"https://&price_max={MAX_PRICE}"
        print(WEBSITE)
        booklooker_bot = BooklookerBot(TELEGRAM_API_KEY)
        booklooker_bot.send_get_request()
    except Exception as e:
        print(e)
