import unicodedata

NUMBER_MAP = {
    "cero": 0,
    "un": 1,
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
    "diez": 10,
    "once": 11,
    "doce": 12,
    "trece": 13,
    "catorce": 14,
    "quince": 15,
    "dieciseis": 16,
    "diecisiete": 17,
    "dieciocho": 18,
    "diecinueve": 19,
    "veinte": 20,
    "treinta": 30,
    "cuarenta": 40,
    "cincuenta": 50,
    "sesenta": 60,
    "setenta": 70,
    "ochenta": 80,
    "noventa": 90,
    "ciento": 100,
    "cien": 100,
    "mil": 1000,
    "millon": 1000000
}

def normalize(words: list[str]) -> list[str]:
    '''Convert keywords to generic forms.  Strip accents, remove plurals.'''
    normalized_words = []

    for word in words.split():
        word = unicodedata.normalize('NFKD',
                                     word.lower()).encode('ascii', 'ignore').decode('utf-8')

        if word.startswith('veinti'):
            suffix = word[6:]
            normalized_words += ['veinte', suffix]
        elif word != 'tres' and word.endswith('es'):
            normalized_words.append(word[:-2])
        elif word == 'quinientos':
            normalized_words += ['cinco', 'cien']
        elif word.endswith('cientos'):
            prefix = word[:-7]

            if prefix == 'nove':
                normalized_words.append('nueve')
            elif prefix == 'sete':
                normalized_words.append('siete')
            else:
                normalized_words.append(prefix)

            normalized_words.append('cien')
        else:
            normalized_words.append(word)

    return normalized_words

def spanish_words_to_number(words):
    total = 0
    temp = 0

    normalized_words = normalize(words)

    for word in normalized_words:
        if word in NUMBER_MAP:
            if word == 'mil':
                total += (temp if temp else 1) * NUMBER_MAP[word]
                temp = 0
            elif word.startswith('cien'):
                temp = (temp if temp else 1) * NUMBER_MAP[word]
            elif word == 'millon':
                total += (temp if temp else 1) * NUMBER_MAP[word]
                temp = 0
            else:
                temp += NUMBER_MAP[word]
        elif word == "y":
            continue

    total += temp

    return total
