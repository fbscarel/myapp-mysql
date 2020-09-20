from flask import Flask
from flask import render_template
import argparse
import mysql.connector
import os
import socket

app = Flask(__name__)

def argtest (cli, env, default):
  if cli:
    return cli
  elif env:
    return env
  else:
    return default

@app.route('/')
def hello():
  try:
    mysql.connector.connect(host=DBHOST, database=DATABASE, user=DBUSER, password=DBPASS)
    status = SUCCESS
    color = '#9eff9a'
  except Exception as e:
    msg = str(e)
    status = FAILURE
    color = '#ff9a9e'

  return render_template('index.html', hostname=socket.gethostname(), dbhost=DBHOST, database=DATABASE, dbuser=DBUSER, dbpass=DBPASS, status=status, color=color)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser = argparse.ArgumentParser(add_help=False)
  parser.add_argument('-h', '--hostname', required=False)
  parser.add_argument('-d', '--database', required=False)
  parser.add_argument('-u', '--username', required=False)
  parser.add_argument('-p', '--password', required=False)
  args = parser.parse_args()

  DBHOST   = argtest (args.hostname, os.environ.get('DBHOST'),   'localhost')
  DBUSER   = argtest (args.username, os.environ.get('DBUSER'),   'root')
  DBPASS   = argtest (args.password, os.environ.get('DBPASS'),   '')
  DATABASE = argtest (args.database, os.environ.get('DATABASE'), 'mysql')

  app.run(host='0.0.0.0', port=80)

