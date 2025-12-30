import redis
import datastore
from datastore import messages
from datastore import access
import json, base64, os, sys
from names_generator import generate_name


r = redis.Redis(host=os.environ['REDIS_HOST'], 
    port=os.environ['REDIS_PORT'], 
    db=os.environ['REDIS_DB'],
    username=os.environ['REDIS_USERNAME'],
    password=os.environ['REDIS_PASSWORD'],
    protocol=3, 
    decode_responses=True
)

def ping():
  try:
    r.ping()
    return True
  except Exception as e:
    raise Exception("Could not connect to database: " + str(e))

def firststep():
  ping()
  password = base64.urlsafe_b64encode(bytes(generate_name(), "utf8"))
  password = password.decode("utf8")
  r.set("firstpw", password)
  r.close()
  sys.stdout.write(f"Your administrator account login is admin and the password is {password}. Go to https://<yourdomain>/supmod")

  
def check_key(key_to_check):
  try:
    result = r.exists(key_to_check)
    return result
  except Exception as e:
    raise Exception(f"Could not verify {key_to_check}: {str(e)}")

def setup():
  r.set("mod_login_count", 150)
  r.rpush("active_auth_codes", "start")
  datastore.create_people_index()
  datastore.create_people_index("moderators")
  datastore.create_people_index("blocked")
  messages.create_message_index()
  access.create_request_access_index()
  r.close()

def remove_firstpw():
  r.delete("firstpw")
  r.set("setup_complete", 1)
  r.close()


def get_mod_login_count():
  num = int(r.get("mod_login_count"))
  print(num)
  r.close()
  return num

def get_active_login_codes():
  codes = r.lrange("active_auth_codes", 0, -1)
  r.close()
  return codes

def remove_code_from_login_codes(code):
  r.lrem("active_auth_codes", 0, code)
  r.close()

def push_new_login_code(code):
  r.rpush("active_auth_codes", code)
  r.close()

def push_mod_login_count(current_mod_login_count):
  r.set("mod_login_count", current_mod_login_count)
  r.close()

