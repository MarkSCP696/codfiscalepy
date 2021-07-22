import json
import datetime
import pandas


# Check if all inserted Data are available
def InsertData():
    out = []
    sName = str(input("Inserisci il nome: "))
    sSurname = str(input("Inserisci il cognome: "))
    sCodiceComune = str(input("Inserisci il comune: "))
    sDataNascita = str(input("Inserisci la data di nascita YYYY-MM-DD : "))
    sSesso = str(input("Inserisci il sesso, M or F: "))
    data_set = {"Nome": sName,  "Cognome": sSurname,
                "CodComune": sCodiceComune, "DataNascita": sDataNascita, "Sesso": sSesso}
    json_dump = json.dumps(data_set)
    if ((sName == '' or sSurname == '' or sCodiceComune == '' or sDataNascita == '' or sSesso == '')):
        out = [0, False]
    else:
        out = [json_dump, True]

    return out


# Ritorna i caratteri di nome e cognome
def GetName3Char(obj, value):
    out = []
    json_object = json.loads(obj)
    name = json_object[value]
    name = name.upper()
    vowel_list = set(["A", "E", "I", "O", "U"])
    numberOfConsonant = countConsonants(name, vowel_list)[0]
    aOfConsonanti = countConsonants(name, vowel_list)[1]
    if numberOfConsonant < 3:
        aOfVocali = countVowels(name, vowel_list)[1]
        missing_vocals = 3 - numberOfConsonant
        for x in range(missing_vocals):
            aOfConsonanti.append(aOfVocali[x])
    return aOfConsonanti[:3]


# Conta le vocali e restituisce quelle utilizzate
def countVowels(user_input, vowel_list):
    out = []
    aVocali = []
    vowels = 0
    for char in user_input:
        if char in vowel_list:
            vowels += 1
            aVocali.append(char)
    out = [vowels, aVocali]
    return out

# Conta le consonanti e restituisce quelle utilizzate


def countConsonants(user_input, vowel_list):
    out = []
    aCons = []
    consonants = 0
    for char in user_input:
        if char not in vowel_list:
            consonants += 1
            aCons.append(char)
    out = [consonants, aCons]
    return out

# Validate date and return Anno 2char , Mese 1char , Giorno 2char


def GetAnnoMeseGiorno(obj, value):
    out = []
    json_object = json.loads(obj)
    dataNascitaIn = json_object[value]
    try:
        datetime.datetime.strptime(dataNascitaIn, "%Y-%m-%d")
        splitted = dataNascitaIn.split("-")
        sSesso = json_object["Sesso"]
        if(sSesso.upper() == "F"):
          splitted[2] = int(splitted[2]) + 40
        convertedMonth = convertMonths(splitted[1])
        out = [splitted[0][2:4], convertedMonth, str(splitted[2]), True]
        if(sSesso.upper() != "F" and sSesso.upper() != "M"):
            out = [0, 0, 0, False]
    except ValueError:
        out = [0, 0, 0, False]

    return out

# Ritorna il comune leggendolo da un file excel e.g. Roma -->H501


def GetComune3Char(obj, value):
    out = []
    comuni_df = pandas.read_excel('./comuni/Comuni.xlsx')
    # Array con la lista dei comuni
    cities = comuni_df.to_dict('records')
    json_object = json.loads(obj)
    ComuneCods = json_object[value]
    # Descrizione del Comune
    keyValList = [ComuneCods]
    expectedResult = [d for d in cities if d['COMUNE'] in keyValList]
    if(len(expectedResult) > 0):
        out = [expectedResult[0]["CODICE"], True]
    else:
        out = [0, False]
    return out


# Converte il mese in una lettera  e.g. 01 --> A
def convertMonths(month):
    switcher = {
        "01": "A",
        "02": "B",
        "03": "C",
        "04": "D",
        "05": "E",
        "06": "H",
        "07": "L",
        "08": "M",
        "09": "P",
        "10": "R",
        "11": "S",
        "12": "T"
    }
    return switcher.get(month, "Invalid month")
