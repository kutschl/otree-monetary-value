# imports
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

doc = "Instructions"


def IntegerField(name, number):
    return models.IntegerField(
        choices=Constants.forms[name]['answers'],
        label=Constants.forms[name]['questions'][number],
        widget=Constants.forms[name]['widget']
    )


def StringField(name, number):
    return models.StringField(
        label=Constants.forms[name]['questions'][number],
        blank=Constants.forms[name]['blank']
    )


class Constants(BaseConstants):
    name_in_url = 'Instructions'
    players_per_group = None
    num_rounds = 1

    fee_participation = c(0)
    fee_questionnaire = c(10)


    # todo: Kontaktdaten einfügen
    contact = {
        'phone': None,
        'email': None
    }

    forms = {
        'CONTROL1': {
            'task': 'Angenommen Sie hätten die Tabelle in einer Entscheidungssituation so ausgefüllt wie in der '
                    ' Abbildung dargestellt. Zudem ist diese Entscheidungssituation für Sie auszahlungsrelevant.'
        },
        'CONTROL1Q1': {
            'answers': [
                [1, 'Kommt drauf an, wie die Investitionsgelegenheit ausgelost wird.'],
                [2, '5€'],
                [3, '2.5€']
            ],
            'questions': {
                1: 'Wie hoch ist Ihre Auszahlung, wenn die <b>letzte </b> Zeile der Tabelle ausgelost wurde?',
            },
            'solution': 2,
            'widget': widgets.RadioSelect
        },
        'CONTROL1Q2': {
            'answers': [
                [1, 'Kommt drauf an, wie die Investitionsgelegenheit ausgelost wird.'],
                [2, '5€'],
                [3, '2.5€']
            ],
            'questions': {
                1: 'Wie hoch ist Ihre Auszahlung, wenn die <b>zweite</b> Zeile der Tabelle ausgelost wurde?'
            },
            'solution': 1,
            'widget': widgets.RadioSelect
        },
        'CONTROL2': {
            'task': 'Angenommen Sie hätten die Tabelle in einer Entscheidungssituation so ausgefüllt wie in '
                    'der Abbildung dargestellt. Zudem ist diese Entscheidungssituation für Sie auszahlungsrelevant.'
        },
        'CONTROL2Q1': {
            'answers': [
                [1, 'Wenn die 3. Zeile der unteren Tabelle ausgelost wurde (1€ Kosten zum Aufheben der Vorauswahl)'],
                [2, 'Wenn ein Betrag von kleiner oder gleich 2€ als Kosten ausgelost wurde.'],
                [3, 'Beide Antworten sind richtig.']
            ],
            'questions': {
                1: 'Wann können Sie die obige Entscheidung selbst treffen?',
            },
            'solution': 3,
            'widget': widgets.RadioSelect
        },
        'CONTROL2Q2': {
            'answers': [
                [1, '5€'],
                [2, '4€'],
                [3, '1€']
            ],
            'questions': {
                1: 'Nehmen Sie an, die <b>dritte</b> Zeile der unteren Tabelle wurde ausgelost, Sie konnten die '
                   'Entscheidung oben also wieder frei treffen (zu Kosten von 1€). Sie haben sich für die '
                   'Investitionsgelegenheit entschieden und erhalten daraufhin 5€ aus der Investitionsgelegenheit. '
                   'Wie hoch ist Ihre Auszahlung?'
            },
            'solution': 2,
            'widget': widgets.RadioSelect
        },
        'CONTROL3': {
            'task': 'Angenommen Sie hätten die Tabelle in einer Entscheidungssituation so ausgefüllt wie in '
                    'der Abbildung dargestellt. Zudem ist diese Entscheidungssituation für Sie auszahlungsrelevant.'
        },
        'CONTROL3Q1': {
            'answers': [
                [1, '2€'],
                [2, '5€'],
                [3, '3€'],
                [4, 'Kommt darauf an wie die Investitionsgelegenheit ausfällt.']
            ],
            'questions': {
                1: 'Wie hoch ist Ihre Auszahlung, wenn in der unteren Tabelle die <b>letzte</b> Zeile ausgelost '
                   'wurde?',
            },
            'solution': 1,
            'widget': widgets.RadioSelect
        },
        'CONTROL3Q2': {
            'answers': [
                [1, 'Die Vorauswahl wird in jedem Fall auszahlungsrelevant sein.'],
                [2, 'Die obige Entscheidung kann wieder frei getroffen werden.'],
                [3, 'Sie sind bereit mindestens 1€ zu bezahlen, um die Vorauswahl aufzuheben.']
            ],
            'questions': {
                1: 'Nehmen Sie an, Sie hätten in <b>jeder</b> Zeile in der unteren Tabelle "nein" angekreuzt. '
                   'Was bedeutet das?'
            },
            'solution': 1,
            'widget': widgets.RadioSelect
        }
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # CONTROL QUESTIONS
    CQ101 = IntegerField('CONTROL1Q1', 1)
    CQ102 = IntegerField('CONTROL1Q2', 1)
    CQ201 = IntegerField('CONTROL2Q1', 1)
    CQ202 = IntegerField('CONTROL2Q2', 1)
    CQ301 = IntegerField('CONTROL3Q1', 1)
    CQ302 = IntegerField('CONTROL3Q2', 1)

