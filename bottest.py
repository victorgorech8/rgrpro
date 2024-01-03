
from forbd import create_connection
import requests
from forbd import execute_read_query
def send_telegram(text: str):
    token = "6692392922:AAETK8Zp5xafcOkRsFxGzM7NDkF2TetPfpo"
    url = "https://api.telegram.org/bot"
    
    url += token
    method = url + "/sendMessage"
    connection = create_connection(
            "sm_app", "postgres", "abc123", "127.0.0.1", "5432"
            )
    connection.autocommit = True
    
    select_users = "SELECT idtelegram from users"
    users = execute_read_query(connection, select_users)

    for user in users:
     channel_id=user
     
     r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

     if r.status_code != 200:
        raise Exception("post_text error")


