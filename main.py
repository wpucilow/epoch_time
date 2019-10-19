#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import os
url = 'https://www.epochconverter.com/'


from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_epochtime():
    response = requests.put(url)
    soup = BeautifulSoup(response.content, "html.parser")
    epoch = soup.find_all('div', id="ecclock", class_="ecclock")
    print(f"epoch: {epoch[0].getText()}")
    return epoch[0].getText()

@app.route('/')
def home():
    epoch = get_epochtime()
    return f"Current epoch time: {str(epoch)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
    