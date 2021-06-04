""" ИСПОЛЬЗОВАНИЕ """
""" pip3 install pycryptodome"""
""" python3 createsign.py <ваш шаблон> """

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import os
import sys

CURDIR = os.getcwd()

def cratesign(file_name):
    # Генерируем новый ключ
    private_key = RSA.generate(1024, os.urandom)
    # Получаем хэш файла
    hesh = SHA256.new()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hesh.update(chunk)

    # Подписываем хэш
    signature = pkcs1_15.new(private_key).sign(hesh)

    # Получаем открытый ключ из закрытого
    pubkey = private_key.publickey().exportKey(format='PEM')
    return pubkey, signature

def writepem(content, path):
    with open(CURDIR + path + '.pem', 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    file = sys.argv[1]
    pk, sign = cratesign(file)
    writepem(pk, '/key')
    writepem(sign, '/sign')
