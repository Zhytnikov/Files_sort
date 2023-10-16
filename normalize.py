import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()


def normalize(name: str,) -> str:
    translate_name = re.sub(r'\W', '_', name.translate(TRANS))
    return translate_name

def normalize(name: str) -> str:
    parts = name.split('.')
    if len(parts) > 1:
        extension = parts[-1]  # Останній елемент - розширення файлу
        name_without_extension = '.'.join(parts[:-1])  
        translated_name = name_without_extension.translate(TRANS)
        return f"{translated_name}.{extension}"
    else:
        # Якщо в імені файлу немає крапки, то просто використовуємо перетворене ім'я без змін.
        return name.translate(TRANS)