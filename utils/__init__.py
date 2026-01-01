import garden
import os
import markdown

PUBLIC_WELCOME_FILE = "./server_src/templates/welcome_public.md"
MEMBER_WELCOME_FILE = "./server_src/templates/welcome_member.md"

def generate_keys(username, email, path):
  keys = garden.create_key_pair(username, email) 
  public_key = keys.pubkey
  try:
    os.makedirs(path)
  except FileExistsError:
    pass
  
  print("Saving keys in " + path)
  fp = open( path + "/pub.key", "w")
  fp.write(str(public_key))
  fp.close()

  fp = open(path + "/sec.key", "w")
  fp.write(str(keys))
  fp.close()
  print("Keys created!")


def get_keyfile_directory():
  path = "/var/keys"
  if os.environ['MODE'] == 'DEBUG':
    path = "./skeys"
  
  return path


def set_welcome_message(welcome_message):
  access_level = os.environ['PUBLIC_ACCESS']
  if welcome_message[0] != '#':
    # add in a h1 heading if the admin forgot 
    welcome_message = '#' + welcome_message
  if access_level == '1':
    fp = open(PUBLIC_WELCOME_FILE, 'w')
    fp.write(welcome_message)
    fp.close()
  else:
    fp = open(MEMBER_WELCOME_FILE, 'w')
    fp.write(welcome_message)
    fp.close()
  


def read_welcome_message(from_file=None):
  access_level = os.environ['PUBLIC_ACCESS']
  if access_level == '1':
    fp = open(PUBLIC_WELCOME_FILE)
    if from_file is None:
      welcome_message = markdown.markdown(fp.read())
    else:
      welcome_message = fp.read()
    fp.close()
  else:
    fp = open(MEMBER_WELCOME_FILE)
    if from_file is None:
      welcome_message = markdown.markdown(fp.read())
    else:
      welcome_message = fp.read()
    fp.close()
  return welcome_message