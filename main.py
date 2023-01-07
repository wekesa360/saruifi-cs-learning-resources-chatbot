import os
import json
import logging
import uvicorn
from urllib import parse
from sarufi import Sarufi
from twilio.rest import Client
from dotenv import load_dotenv
from fastapi import FastAPI, Request

load_dotenv()

# required credentials set in environment variables
username = os.environ.get('SARUFI_USERNAME')
password = os.environ.get('SARUFI_PASSWORD')
account_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
account_sid = os.environ.get('TWILIO_SID')

logging.basicConfig(level=logging.DEBUG)
# using helper libraries, authenticate
client=Client(account_sid, account_auth_token)
sarufi = Sarufi(username, password)

app = FastAPI()

# log message flow to messageResponse.log
def log_message(message, response):
    f = open("messageResponse.log", "a")
    f.write(f"\nMessage: {message} \n {response}")
    f.flush()

# webhook api endpoint
@app.post("/webhook_endpoint")
async def message_endpoint(request: Request):
    data = await request.body()
    # convert url and byte format to string
    parsed_data = parse.parse_qs(data.decode('utf-8'))
    json_data = json.dumps(parsed_data)
    # convert string to json
    message_dict = json.loads(json_data)
    # sarufi bots
    bots = sarufi.bots()
    Nalah=bots[0]
    # send message from request to Nalah(sarufi bot)
    response = Nalah.respond(message_dict["Body"][0])
    # get response and log with message
    log_message(message_dict["Body"], response["message"])
    # loop through list and send each item through twilio
    i = 0
    while i < len(response["message"]):
        message = client.messages.create(
                                    body=response["message"][i],
                                    from_=message_dict["To"],
                                    to= message_dict["From"])
        print(message.sid)
        i += 1

if __name__ == '__main__':
    uvicorn.run(app, debug=True)