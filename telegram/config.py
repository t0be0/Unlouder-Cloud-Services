# CONFIG

import os


## EDIT (Required) ##############################################################################
# https://my.telegram.org/apps

api_id = int('API_ID') # API ID  (int)
api_hash = str("API_HASH") # API HASH  (str)
bot_token = str("BOT_TOKEN from @BotFather") # BOT TOKEN (str)
# channel_id = int('-100') # CHANNEL ID [create channel, send mssg and forward message from channel to @userinfobot) (int)
channel_id = str('channel username without @')


## EDIT (Optional) ##############################################################################

download_dir = str(os.path.join(os.getcwd(), 'downloads'))
sessions_dir = str(os.path.join(os.getcwd(), 'sessions'))
files_dir = str(os.path.join(os.getcwd(), 'files'))
status_logs_dir = str(os.path.join(os.getcwd(), 'temp'))

def CheckDirExistence(dir):

    if not os.path.isdir(dir):
        os.mkdir(dir)

CheckDirExistence(download_dir)
CheckDirExistence(sessions_dir)
CheckDirExistence(files_dir)
CheckDirExistence(status_logs_dir)