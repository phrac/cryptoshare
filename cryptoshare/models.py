from django.db import models

import hashlib
from Crypto.Cipher import AES
import os, base64

from cryptoshare.pkcs7 import PKCS7Encoder

class Document(models.Model):
    ciphertext = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def encrypt(self, raw, ukey):
        pad = PKCS7Encoder()
        key = hashlib.sha256(ukey).digest()
        iv = os.urandom(16)
        msg = pad.encode(raw)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(msg))
        

    def decrypt(self, ukey=None):
        unpad = PKCS7Encoder()
        msg = base64.b64decode(self.ciphertext)
        iv = msg[:16]
        key = hashlib.sha256(ukey).digest()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        try:
            txt = unpad.decode((cipher.decrypt(msg[16:])))
            self.views += 1
            self.save()
        except:
            txt = "Incorrect Key"
        return txt
        

