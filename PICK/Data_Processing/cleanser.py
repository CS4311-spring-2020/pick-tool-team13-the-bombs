import logging
import re
import unicodedata

from ftfy import fix_text

from unidecode import unidecode

SINGLE_QUOTES = ["‘", "‛", "’", "❛", "❜", "`", "´", "‘", "’"]
DOUBLE_QUOUTES = [ "«","‹","»","›","„","“","‟","”","❝","❞","❮","❯","〝","〞","〟","＂",]

def fix_quotes(str):
    str = re.compile("|".join(SINGLE_QUOTES)).sub("'", str)
    str = re.compile("|".join(DOUBLE_QUOUTES)).sub('"', str)
    return str

def fix_unicode(str):
    str = str.encode().decode("unicode-escape")
    return fix_text(str)

def to_ascii(str):
    return unidecode(str)

def remove_extra_spaces(str):
    return re.compile(r"\s+").sub(" ", str)

def cleanse(str, bad_quotes=True, bad_unicode=True, bad_ascii=True, bad_extra_spaces=True):
    if(bad_quotes):
        str = fix_quotes(str)
    if(bad_unicode):
        str = fix_unicode(str)
    if(bad_ascii):
        str = to_ascii(str)
    if(bad_extra_spaces):
        str = remove_extra_spaces(str)
    return str

def file_cleanse(filename, outputFilename, bad_quotes=True, bad_unicode=True, bad_ascii=True, bad_extra_spaces=True):
    lines = []
    try:
        file = open(filename, 'r')
    except IOError:
        print("Could not open file")
        return
    lines = file.readlines()
    try:
        file2 = open(outputFilename, 'w')
    except IOError:
        print('Unable to open', outputFilename)
        return
    for str in lines:
        file2.write(cleanse(str, bad_quotes,bad_unicode,bad_ascii,bad_extra_spaces))


