import json
import datetime
import pandas
import sys
# My custom functions
import Util.functions

# Main Method ####################
result = Util.functions.InsertData()
if(not(result[1])):
    print("Inserire tutti i campi obbligatori")
else:
    aSurname = Util.functions.GetName3Char(result[0], "Cognome")
    aName = Util.functions.GetName3Char(result[0], "Nome")
    aValidate = Util.functions.GetAnnoMeseGiorno(result[0], "DataNascita")
    if(not(aValidate[3])):
        print("Inserisci la data nel seguente formato YYYY-MM-DD ed il sesso M o F")
    else:
        aAnno = aValidate[0]
        aMese = aValidate[1]
        aGiorno = aValidate[2]
        ValidateComune = Util.functions.GetComune3Char(result[0], "CodComune")
        if(not(ValidateComune[1])):
            print("Codice comune non esistente")
        else:
            aComune = ValidateComune[0]
            SurnameJoined = ''.join(aSurname)
            NameJoined = ''.join(aName)
            output = SurnameJoined + NameJoined + aAnno + aMese + aGiorno + aComune + "N"
            print("CODICE FISCALE : " + output)
