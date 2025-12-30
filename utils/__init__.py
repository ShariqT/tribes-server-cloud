import garden
import os


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


