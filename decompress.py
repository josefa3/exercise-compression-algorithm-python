# !/usr/bin/python
# coding=utf-8
import re
from compress import symbols

def decompress(compressed_content):

    decompressed_content = compressed_content 

    for i, emoji in symbols.items():  
        decompressed_content = decompressed_content.replace(emoji, i)
        # la funcion replace en cada iteracion sobre escribe el string. Si uso content en vez de descompressed
        # se va a cambiar la palabra por el emoji, pero en la siguiente iteración va a sobreescribir el anterior
        # de modo que debo usar este último para que al sobre escribirse en cada iteración ya esté guardado el cambio
    return compressed_content
    