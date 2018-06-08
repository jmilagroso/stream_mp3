#!/usr/local/bin/python

import os
import urllib.parse
from sanic import Sanic
from sanic.response import json
from sanic import response
from sanic.response import text

# Instantiate Sanic
app = Sanic()

# Base URL
CONST_BASE_URL = "http://localhost:8181/"
# Directory where the mp3 files resides
CONST_FILES_DIR = "/home/jay/Music/";

# URL Encodes string
def urlencode(str):
    return urllib.parse.quote_plus(str)

# URL Decodes string
def urldecode(str):
    return urllib.parse.unquote_plus(str)

# Generate URL
def generate_url(filename):
	return "<a target=\"_blank\" href=\""+ CONST_BASE_URL + "play/" + urlencode(filename)  + "\">"  +  filename + "</a><br>"

# List mp3 files URL
@app.route('/')
def handle_request(request):
    s = ""
    for root, dirs, files in os.walk(CONST_FILES_DIR):
        for filename in files:
            s += generate_url(filename)

    return response.html(s)

# Play song URL
@app.route('/play/<song>')
async def handle_request(request, song):
    return await response.file_stream(os.path.abspath(CONST_FILES_DIR + urldecode(str(song))))

# Main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, workers=4)
