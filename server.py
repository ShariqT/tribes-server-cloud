

import json
import pickle
import garden
import argparse
import redis
import subprocess
import datastore
from datastore import messages
from dotenv import load_dotenv
import os
import pyotp
from utils.dbsetup import setup, firststep, check_key
load_dotenv()

parser = argparse.ArgumentParser(prog="Tribes", description="Tribes Server Admin")
parser.add_argument("--setup-db", action='store_true')
parser.add_argument("--show-admin-pw", action='store_true')
parser.add_argument('--run-dev-server', action='store_true')
parser.add_argument('--run-server', action='store_true')

args = parser.parse_args()
os.environ['OTP_KEY'] = pyotp.random_base32()

if args.show_admin_pw is True:
  firststep()

if args.setup_db is True:
  setup()


if args.run_dev_server is True:
  os.environ['MODE'] = 'DEBUG'
  if len(os.listdir("./skeys")) == 0:
    firststep()
  subprocess.call(f"flask --app server_src --debug run --port {os.environ['PORT']}", shell=True)

if args.run_server is True:
  from waitress import serve
  from server_src import app
  os.environ['MODE'] = 'PROD'
  print(f"Running production server on port {os.environ['PORT']}")
  serve(app, host='0.0.0.0', port=os.environ['PORT'])




