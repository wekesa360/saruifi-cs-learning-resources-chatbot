## Nalah
 A Computer Science resource chatbot built on [Sarufi](https://sarufi.io/). Sarufi is a low to no-code Conversational AI builder platform that will provides NLP infrastructure to create and deploy a chatbot.

The application uses a [**sarufi-python-sdk**](https://github.com/sarufi-io/sarufi-python-sdk)

Nalah, is integrated with whatsapp using **Twilio**.

### Installation
Set up the a virtual environment, e.g when using **python-virtualenv**
```
virtualenv venv
```

Install all the requirements from the **requirements.txt** file
```
pip install -r requirements.txt
```

Set up the required Environment variables in this case:

 ```
    SECRET_KEY = 'Some unique string'

    SARUFI_USERNAME = 'Sarufi account username'

    SARUFI_PASSWORD = 'Sarufi account password'

    TWILIO_SID = 'Twilio Account SID'

    TWILIO_AUTH_TOKEN  = 'Twilio Account Authentication token'
 ```

 Using **uvicorn** as the server application **run**

 ```
 uvicorn main:app --reload
 ```

### Technologies used

- [Flask](https://flask.palletsprojects.com/)
- [Twilio](https://www.twilio.com/)
- [Sarufi](https://sarufi.io/)

### Screenshots

![screenshot](https://github.com/wekesa360/saruifi-cs-learning-resources-chatbot/blob/main/screenshots/Screenshot_1.png?raw=true)