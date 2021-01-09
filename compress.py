 # !/usr/bin/python
# coding=utf-8
import re

symbols = {
#   key             :   symbols[key]
    "is better than":   "😴",
    "If the implementation":   "🤯",
    "practicality"  :   '🤩',
    "better"        :   '😅',
    "than"          :   '😘',
    "Although"      :   "🥺",
    "to explain,"   :   "🤐",
}

def compress(content):

    compressed_content = content

    for i, emoji in symbols.items():
        compressed_content = compressed_content.replace(i, emoji)
    print(compressed_content)

    return content