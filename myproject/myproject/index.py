# -*- coding: utf-8 -*-

import os
import sys
import json

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "lindo":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

    data = request.get_json()

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text

                    if(message_text=="1"):
                        send_message(sender_id,"Por favor, preencha o formulario deste link e boa sorte")
                    elif(message_text=="2"):
                        send_message(sender_id,"Por favor, envie o seu orçamento contendo o máximo de informações que voce tiver para contato@estudiopegrande.com.br")
                    elif(message_text=="3"):
                        send_message(sender_id,"Ok, lá vai uma referencia que gostamos muito!")
                    else:
                        send_message(sender_id,"Ola! Meu nome é Walter e sou assistente digital do Estúdio Pé Grande.")
                        send_message(sender_id,"Como posso ajudálo "+"nome")
                        send_message(sender_id,"Tecle '1' Caso você deseje enviar o seu portifólio/currículo.")
                        send_message(sender_id,"Tecle '2' Caso você deseje enviar um orçamento.")
                        send_message(sender_id,"Tecle '3' Caso vocë deseje ver uma referência aleatória de animação.")

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


def send_message(recipient_id, message_text):

   # log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": "EAAVKsClMLIYBALKPYsDXc4lmzJIuRx7g1lnWdWLGnlkaXPN13EcVe9hHwTqPaJ6mIFgmHcvKwcN9X9ETdWv70YxD2kmY4R2GLl9H037dfhiZCLVVDmvANgltcfcVdumNsTi3p9lrsPSjOg5PdYxUiuc1rSzYfMZAuM1OyD0gZDZD"
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

def send_image(recipient_id, url):

   # log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": "EAAVKsClMLIYBALKPYsDXc4lmzJIuRx7g1lnWdWLGnlkaXPN13EcVe9hHwTqPaJ6mIFgmHcvKwcN9X9ETdWv70YxD2kmY4R2GLl9H037dfhiZCLVVDmvANgltcfcVdumNsTi3p9lrsPSjOg5PdYxUiuc1rSzYfMZAuM1OyD0gZDZD"
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment":{
                "type":"image",
                "payload":{
                    "url":url
                }
            }
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


if __name__ == '__main__':
    app.run(debug=True)