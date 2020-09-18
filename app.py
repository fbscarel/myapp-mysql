from flask import Flask
from flask import render_template
import pymysql.cursors
import argparse
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html', hostname=socket.gethostname(), dbhost=DBHOST, dbuser=DBUSER, dbpass=DBPASS)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-h', '--host', required=False)
  parser.add_argument('-u', '--user', required=False)
  parser.add_argument('-p', '--pass', required=False)
  args = parser.parse_args()

#fixthis
  if os.environ.get('DBHOST'):
    DBHOST = os.environ.get('DBHOST')
  else:
    DBHOST = args.dbhost

  if os.environ.get('DBHOST'):
    DBHOST = os.environ.get('DBHOST')
  else:
    DBHOST = args.dbhost

  if os.environ.get('DBHOST'):
    DBHOST = os.environ.get('DBHOST')
  else:
    DBHOST = args.dbhost

  app.run(host='0.0.0.0', port=80)

