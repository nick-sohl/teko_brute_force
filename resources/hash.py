import hashlib

def calculate_md5(text):
  # Erstelle ein hashlib Objekt für den MD5 Algorithmus
  md5_hash = hashlib.md5()

  # Codiere den Text in Bytes, da hashlib nur Bytes akzeptiert
  encoded_text = text.encode('utf-8')

  # Aktualisiere den Hash mit dem codierten Text
  md5_hash.update(encoded_text)

  # Gib den Hash als hexadezimale Zeichenkette zurück
  return md5_hash.hexdigest()

alphabet_lowercase = ['a']

# Beispielaufruf:
text = ("abcdef")
md5_hash = calculate_md5(text)
print(md5_hash)