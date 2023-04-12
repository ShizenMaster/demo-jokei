from flask import Flask
from threading import Thread

app = Flask('app')

@app.route('/')
def maun():
  return 'Bot are working!'

def run():
  app.run(host="0.0.0.0", port=8080)

def server():
  servers = Thread(target=run)
  servers.start()