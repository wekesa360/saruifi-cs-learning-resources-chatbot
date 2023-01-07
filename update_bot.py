from sarufi import Sarufi
from dotenv import load_dotenv
import os

load_dotenv()
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

sarufi = Sarufi(username, password)

def update_sarufi_bot():
    updated_Nalah_bot = sarufi.update_from_file(
                            id=331,
                            intents="data/intents.yaml",
                            flow="data/flows.yaml",
                            metadata="data/metadata.yaml",
                        )
    return updated_Nalah_bot.data


if __name__ == "__main__":
    print(update_sarufi_bot())

