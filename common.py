# 2022 - YemekSepeti Python Web Development BootCamp
# common functions and constants

import re

class RE:

    defaultNone = "None"
    defaultZero = "0"
    defaultYear = "1000"
    defaultMonth = "01"
    defaultDay = "01"
    defaultAP = "1"
    
    @staticmethod
    def verifyUsernamelk(username, email):
        return "1" if username in email else "0"

    @staticmethod
    def verifyEmailuserlk(username, email):
        return "1" if username in email else "0"
        
    @staticmethod
    def verifyEmail(email):
        regex = '^([a-zA-Z0-9.!#$%`*+/=?^_{|}~-]|\d)+@([a-z]|\d\-)+(\.([a-z]|\d|-)+)+$'
        return re.match(regex, str(email).lower())
    
    @staticmethod   
    def verifyDogumyil(dogumyil):
        pass

    @staticmethod
    def verifyDogumay(dogumay):
        pass

    @staticmethod
    def verifyDogumgun(dogumgun):
        pass


