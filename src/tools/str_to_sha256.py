import hashlib

def StrToSha256(str: str):
  h = hashlib.new('sha256')
  h.update(bytes(str, encoding='utf8'))
  return h.hexdigest()
