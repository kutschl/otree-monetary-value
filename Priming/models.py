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

doc = "Priming"


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
    name_in_url = 'Priming'
    players_per_group = 3
    num_rounds = 1

    fee_participation = c(0)
    fee_questionnaire = c(10)

    # todo: Kontaktdaten einfügen
    contact = {
        'phone': None,
        'email': None
    }

    forms = {
        'NEUTRAL1': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                1: 'Sind/Waren Sie Student(in) an der Universität Bonn?',
                2: 'Wussten Sie, dass die Universität Bonn 2018 200-jähriges Jubiläum feierte?',
                3: 'Ist Ihnen die Exzellenzinitiative bekannt?'
            },
            'task': 'Bitte beantworten Sie die folgenden Fragen.',
            'widget': widgets.RadioSelectHorizontal
        },
        'NEUTRAL2': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Es ist wichtig die Geschichte einer Universität zu kennen um deren Gegenwart und Zukunft '
                   'zu beurteilen.',
                2: 'Es sollte mehr Wert darauf gelegt werden die Geschichte einer Universität an Studierende '
                   'und MitarbeiterInnen zu vermitteln'
            },
            'task': 'Wie sehr stimmen Sie den folgenden 2 Aussagen zu.',
            'label': {
                1: 'Stimme überhaupt nicht zu',
                2: 'Stimme voll und ganz zu'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'USEFUL1': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                1: 'Gehören Sie selbst zu einer Risikogruppe?',
                2: 'Haben Sie regelmäßig Kontakt zu Personen, die zu einer Risikogruppe gehören?',
                3: 'Kennen Sie Personen, die an COVID-19 erkrankt sind?'
            },
            'task': 'Bitte beantworten Sie die folgenden Fragen.',
            'widget': widgets.RadioSelectHorizontal
        },
        'USEFUL2': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Während der ersten Corona Welle Sorgen habe ich mir große Sorgen gemacht über meine eigene '
                   'Gesundheit und/oder über die Gesundheit meiner Freunde und/oder meiner Familie?',
                2: 'Während der ersten Corona Welle hatte ich Angst davor, dass das Gesundheitssystem '
                   'zusammenbrechen könnte und somit sowohl Corona-Erkrankte als auch andere Notfälle nicht '
                   'mehr ausreichend versorgt werden könnten.'
            },
            'task': 'Wie sehr stimmen Sie den folgenden 2 Aussagen zu.',
            'label': {
                1: 'Stimme überhaupt nicht zu',
                2: 'Stimme voll und ganz zu'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'RESTRICT1': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                1: 'Sind Sie im beruflichen Kontext oder in Ihrer Ausbildung (Schule, Studium) von den '
                   'Maßnahmen der Pandemie betroffen (gewesen)',
                2: 'Kennen Sie Personen, die durch die Maßnahmen der Pandemie ihren Job verloren haben oder '
                   'nicht arbeiten konnten?',
                3: 'Haben Sie durch die Maßnahmen der Pandemie finanzielle Einbußen erlebt?'
            },
            'task': 'Bitte beantworten Sie die folgenden Fragen.',
            'widget': widgets.RadioSelectHorizontal
        },
        'RESTRICT2': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Ich oder mir nahestehende Personen haben durch die Maßnahmen der Pandemie in der ersten '
                   'Welle mentale Beschwerden erlebt, wie zum Beispiel Einsamkeit oder depressive Zustände?',
                2: 'Ich habe mir während der ersten Corona Welle große Sorgen gemacht über meine eigene '
                   'berufliche Zukunft und/oder über die berufliche Zukunft meiner Freunde bzw. meiner Familie?'
            },
            'task': 'Wie sehr stimmen Sie den folgenden 2 Aussagen zu.',
            'label': {
                1: 'Stimme überhaupt nicht zu',
                2: 'Stimme voll und ganz zu'
            },
            'widget': widgets.RadioSelectHorizontal
        }
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # PRIMING ROLE
    def set_priming(self):
        if self.id_in_group == 1:
            return 'NEUTRAL'
        if self.id_in_group == 2:
            return 'RESTRICT'
        if self.id_in_group == 3:
            return 'USEFUL'

    PRIMING_ROLE = models.StringField()

    # PRIMING QUESTIONS NEUTRAL
    PN01 = IntegerField('NEUTRAL1', 1)
    PN02 = IntegerField('NEUTRAL1', 2)
    PN03 = IntegerField('NEUTRAL1', 3)
    PN04 = IntegerField('NEUTRAL2', 1)
    PN05 = IntegerField('NEUTRAL2', 2)

    # PRIMING QUESTIONS USEFUL
    PU01 = IntegerField('USEFUL1', 1)
    PU02 = IntegerField('USEFUL1', 2)
    PU03 = IntegerField('USEFUL1', 3)
    PU04 = IntegerField('USEFUL2', 1)
    PU05 = IntegerField('USEFUL2', 2)

    # PRIMING QUESTIONS RESTRICT
    PR01 = IntegerField('RESTRICT1', 1)
    PR02 = IntegerField('RESTRICT1', 2)
    PR03 = IntegerField('RESTRICT1', 3)
    PR04 = IntegerField('RESTRICT2', 1)
    PR05 = IntegerField('RESTRICT2', 2)
