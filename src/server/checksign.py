from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

def check(content, k_pem, s_pem):
    pubkey = RSA.importKey(k_pem)
    signature = s_pem

    hesh = SHA256.new(content)

    check_sign = False
    try:
        pkcs1_15.new(pubkey).verify(hesh, signature)
        check_sign = True
        return check_sign
    except Exception as e:
        print(e)
        return check_sign  