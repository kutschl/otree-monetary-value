# imports
import math
from decimal import Decimal

from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

doc = "Intro"


class Constants(BaseConstants):
    name_in_url = 'Intro'
    players_per_group = None
    num_rounds = 1

    participation_fee = 0

    contact = {
        'phone': '',
        'email': ''
    }

    Alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    AlphabetDict = {}
    for n, l in enumerate(Alphabet):
        AlphabetDict.update([(l, n + 10)])


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    EMAIL_VALID = models.StringField(
        label='E-Mail'
    )

    VORNAME = models.StringField(
        label='Vorname'
    )

    NACHNAME = models.StringField(
        label='Nachname'
    )

    STRASSE = models.StringField(
        label='Straße'
    )

    HAUSNUMMER = models.StringField(
        label='Hausnummer'
    )

    PLZ = models.StringField(
        label='Postleitzahl'
    )

    ORT = models.StringField(
        label='Ort'
    )

    IBAN = models.StringField(
        label='IBAN'
    )

    BIC = models.StringField(
        label='BIC'
    )

    def IBAN_error_message(self, value):
        reordered_iban = list(value)[4:len(value)] + list(value)[0:4]
        numeric_iban = ""
        invalid_chars = 0
        for l in range(len(value)):
            if reordered_iban[l] == " ":
                return "Bitte verwenden Sie keine Leerzeichen."
            if reordered_iban[l] in Constants.Alphabet:
                numeric_iban += str(Constants.AlphabetDict[reordered_iban[l]])
            elif reordered_iban[l] in [str(x) for x in range(10)]:
                numeric_iban += reordered_iban[l]
            else:
                invalid_chars += 1
        if invalid_chars > 0:
            return "Ihre Eingabe enthält ungültige zeichen. Bitte verwenden Sie nur Ziffern und Großbuchstaben."
        elif round(Decimal(numeric_iban) - math.floor(Decimal(numeric_iban) / 97) * 97) != 1:
            return "Die IBAN ist ungültig. Bitte überprüfen Sie Ihre Eingabe."





