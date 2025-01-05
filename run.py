from flask import Flask
from routes import main
from handler import errors
import os

# For BOT SESSION
from pyrogram import Client
from telegram.config import api_id, api_hash, bot_token

if not os.path.isfile(os.path.join(os.getcwd(), 'sessions', 'my_account.session')):
    print("[+] Creating Telegram Session File\n")
    _app = Client("my_account", workdir = os.path.join(os.getcwd(), 'sessions'), api_id=api_id, api_hash=api_hash)
    _app.start()
    _app.stop()

####################################################################


App = Flask(__name__)
App.register_blueprint(main)
App.register_blueprint(errors)

try:
    SERVER_PORT = os.getConfig('SERVER_PORT')
    if len(SERVER_PORT) == 0:
        raise KeyError
except:
    SERVER_PORT = 8080

if __name__ == '__main__':
	App.run(debug=True, host='0.0.0.0', port=SERVER_PORT)