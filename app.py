from flask import Flask, request # flask's request can used to get these POST request 
from twilio.twiml.messaging_response import MessagingResponse # Twilio expects an response given in TwiML(Xml based) language. This class can be used to covert our respose into TwiML

app = Flask(__name__) # Initialte Our Flask App

@app.route("/") # if we open the '/' route
def hello(): 
    return "Hello, World!"

@app.route("/bot", methods=['POST']) # Our '/bot' route and this will only listen to POST requests
def bot():
    # Fetch the message
    message = request.form.get('Body') # Get the message sent by other user(The request will have a key of 'Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You just said: {}".format(message)) 

    return str(resp) # Return the resp

if __name__ == "__main__":
    app.run(debug=False)
