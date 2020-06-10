from bs4 import BeautifulSoup
import requests as req
import re
import json
from http.server import BaseHTTPRequestHandler
usr = "yg"

url = f'https://github.com/sponsors/{usr}'
resp = req.get(url)


def getSponsorNames():
    if resp.history:
        sponsors = None
    else:
        htmlGH = BeautifulSoup(resp.text, 'html.parser')
        count = htmlGH.select("div.mr-1 > a > img")
        users = []
        for handle in count:
            users.append({"handle": handle['alt'].replace('@', ''),"avatar": handle['src']})
        d = users
        d = json.dumps(d)
        return d
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        message = getSponsorNames()
        self.wfile.write(str(message).encode())
        return