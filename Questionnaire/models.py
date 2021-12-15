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

doc = "Questionnaire"


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
    name_in_url = 'Questionnaire'
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
        'FRAGEN1': {
            'task': 'Bitte beantworten Sie die folgenden Fragen',
        },
        'FRAGEN1Q1': {
            'answers': list(range(1, 12)),
            'questions': {
                1: 'Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder '
                   'versuchen Sie, Risiken zu vermeiden?'
            },
            'label': {
                1: 'Gar nicht risikobereit',
                2: 'Sehr risikobereit'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN1Q2': {
            'answers': list(range(1, 12)),
            'questions': {
                2: 'Wie hoch ist Ihre Bereitschaft, auf etwas zu verzichten, um in Zukunft darauf zu profitieren, '
                   'wenn es um finanzielle Entscheidungen geht?',
            },
            'label': {
                1: 'Keine Bereitschaft',
                2: 'Sehr hohe Bereitschaft'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN2': {
            'answers': list(range(1, 12)),
            'questions': {
                1: 'Wie sehr wären Sie bereit, jemanden zu bestrafen, der <b>Sie</b> unfair behandelt, selbst wenn '
                   'dies für Sie negative Konsequenzen hat? ',
                2: 'Wie sehr wären Sie bereit, jemanden zu bestrafen, der <b>andere</b> unfair behandelt, selbst wenn '
                   'dies für Sie Kosten verursachen würde?',
                3: 'Wie sehr wären Sie bereit, für einen guten Zweck zu geben, ohne etwas als Gegenleitung zu erwarten?'
            },
            'task': 'Bitte beantworten Sie die folgenden Fragen',
            'label': {
                1: 'Keine Bereitschaft',
                2: 'Sehr hohe Bereitschaft'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN3': {
            'answers': list(range(1, 12)),
            'questions': {
                1: 'Wenn mir jemand einen Gefallen tut, bin ich bereit ihn zu erwidern?',
                2: 'Wenn ich sehr ungerecht behandelt werde, räche ich mich bei der ersten Gelegenheit, selbst'
                   'wenn Kosten entstehen, um das zu tun.',
                3: 'Ich vermute, dass Leute nur die besten Absichten haben.'
            },
            'task': 'Wie gut beschreibt jede der nachfolgenden Aussagen Sie als Person?',
            'label': {
                1: 'Beschreibt mich überhaupt nicht',
                2: 'Beschreibt mich perfekt'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN4': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Ich bin gut darin, Versuchungen zu widerstehen.',
                2: 'Es fällt mir schwer, schlechte Gewohnheiten abzulegen.',
                3: 'Ich bin faul.',
                4: 'Ich sage unangemessene Dinge.',
                5: 'Ich tue manchmal Dinge, die schlecht für mich sind, wenn sie mir Spaß machen.',
                6: 'Ich wünschte, ich hätte mehr Selbstdisziplin.',
                7: 'Angenehme Aktivitäten und Vergnügen hindern mich manchmal daran, meine Arbeit zu machen.',
                8: 'Es fällt mir schwer, mich zu konzentrieren.',
                9: 'Ich kann effektiv auf langfristige Ziele hinarbeiten.',
                10: 'Manchmal kann ich mich selbst nicht daran hindern, etwas zu tun, obwohl ich weiß, dass es '
                    'falsch ist.',
                11: 'Ich handle oft ohne alle Alternativen durchdacht zu haben.',
                12: 'Ich lehne Dinge ab, die schlecht für mich sind.',
                13: 'Andere würden sagen, dass ich eine eiserne Selbstdisziplin habe.'
            },
            'task': 'Bitte geben Sie an, inwieweit die folgenden Aussagen normalerweise auf Sie zutreffen.',
            'label': {
                1: 'völlig unzutreffend',
                2: 'trifft ganz genau zu'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN5': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Wie mein Leben verläuft, hängt von mir selbst ab.',
                2: 'Im Vergleich mit anderen habe ich nicht das erreicht, was ich verdient habe.',
                3: 'Was man im Leben erreicht, ist in erster Linie eine Frage von Schicksal und Glück.',
                4: 'Wenn man sich sozial und politisch engagiert, kann man die sozialen Verhältnisse beeinflussen.',
                5: 'Ich mache häufig die Erfahrung, dass andere über mein Leben bestimmen.',
                6: 'Erfolg muss man sich hart erarbeiten.',
                7: 'Wenn ich im Leben auf Schwierigkeiten stoße, zweifle ich oft an meinen Fähigkeiten.',
                8: 'Welche Möglichkeiten ich im Leben habe, wird von sozialen Umständen bestimmt.',
                9: 'Wichtiger als alle Anstrengungen sind die Fähigkeiten, die man mitbringt.',
                10: 'Ich habe wenig Kontrolle über die Dinge, die in meinem Leben passieren.'
            },
            'task': 'Die folgenden Aussagen kennzeichnen verschiedene Einstellungen zum Leben und zur Zukunft.'
                    'In welchem Maß stimmen Sie persönlich den einzelnen Aussagen zu?',
            'label': {
                1: 'Stimme nicht zu',
                2: 'Stimme voll zu'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN6': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Ich bin eher zurückhaltend.',
                2: 'Ich schenke anderen leicht Vertrauen, glaube an das Gute im Menschen.',
                3: 'Ich bin bequem, neige zur Faulheit.',
                4: 'Ich bin entspannt, lasse mich durch Stress nicht aus der Ruhe bringen.',
                5: 'Ich habe nur wenig künstlerisches Interesse.',
                6: 'Ich gehe aus mir heraus, bin gesellig.',
                7: 'Ich neige dazu, andere zu kritisieren.',
                8: 'Ich erledige Aufgaben gründlich.',
                9: 'Ich werde leicht nervös und unsicher.',
                10: 'Ich habe eine aktive Vorstellungskraft.'
            },
            'task': 'Bitte geben Sie an, wie gut die Aussage auf Sie zutrifft.',
            'label': {
                1: 'Trifft überhaupt nicht zu',
                2: 'Trifft voll und ganz zu'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN7': {
            'questions': {
                1: 'Um was ging es in diesem Experiment Ihrer Meinung nach?',
                2: 'Bitte nennen Sie Gründe für Ihre Entscheidung in den Situationen mit Vorauswahl.'
            },
            'task': 'Bitte beantworten Sie die folgenden Fragen in Stichpunkten.',
            'blank': False
        },
        'FRAGEN8': {
            'task': 'In den folgenden Fragen geht es um den Block an Entscheidungssituationen, in denen Ihre '
                    'Entscheidung durch eine Vorauswahl eingeschränkt wurde.'
        },
        'FRAGEN8Q1': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Haben Sie sich in den Entscheidungssituationen mit Vorauswahl eingeschränkt gefühlt?'
            },
            'label': {
                1: 'Nein, gar nicht',
                2: 'Ja, sehr'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN8Q2': {
            'answers': [
                [1, 'nicht oder kaum gestört'],
                [2, 'prinzipiell gestört'],
                [3, 'nur gestört, wenn meine bevorzugte Wahl nicht zur Verfügung stand']
            ],
            'questions': {
                2: 'Die Vorauswahl hat mich ...'
            },
            'widget': widgets.RadioSelect
        },
        'FRAGEN9': {
            'task': {
                1: 'In den folgenden Fragen geht es um den Block an Entscheidungssituationen, in denen Ihre '
                    'Entscheidung durch eine Vorauswahl eingeschränkt wurde.',
                2: 'Ich habe die Vorauswahl wahrgenommen als ...',
                3: 'Ich welchen der folgenden Situationen kann es aus Ihrer persönlichen Sicht gerechtfertigt '
                   'sein, wenn der Staat individuellen Handlungsspielraum einschränkt?'
            }
        },
        'FRAGEN9Q1_Q3': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                1: 'Eingriff in meine Autonomie und Entscheidungsfreiheit',
                2: 'Einschränkung meines Handlungsspielraumes für die spezifischen Situationen',
                3: 'Gar nicht/kaum wahrgenommen'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN9Q4': {
            'questions': {
                4: 'Sonstiges'
            },
            'blank': True
        },
        'FRAGEN9Q5_Q14': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                5: 'Umweltschutz',
                6: 'Rauchen',
                7: 'Glücksspiel',
                8: 'Schulbesuch',
                9: 'Fleischkonsum',
                10: 'Sparen/Altersvorsorge',
                11: 'Cannabiskonsum',
                12: 'Konsum von harten Drogen wie z.B. Heroin',
                13: 'Autofahren',
                14: 'Gesundheitsvorsorge'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN9Q15': {
            'questions': {
                15: 'Sonstiges'
            },
            'blank': True
        },
        'FRAGEN10': {
            'task': 'Bitte beantworten Sie die folgenden Fragen.'
        },
        'FRAGEN10Q1': {
            'answers': list(range(1, 5)),
            'questions': {
                1: 'Wie viel Vertrauen haben Sie generell in die Regierung / in die Politik die richtigen Maßnahmen '
                   'in der Reaktion auf eine Krisensituation zu erlassen?'
            },
            'label': {
                1: 'Überhaupt kein Vertrauen',
                2: 'Volles Vertrauen'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN10Q2': {
            'answers': list(range(1, 5)),
            'questions': {
                2: 'Wie sehr wird Ihr Alltag momentan negativ von Corona beeinflusst?'
            },
            'label': {
                1: 'Überhaupt nicht beeinträchtigt',
                2: 'Sehr stark beeinträchtigt'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN10Q3': {
            'answers': list(range(1, 5)),
            'questions': {
                3: 'Wie sehr haben Sie sich generell über die gesamte Zeit der Pandemie hinweg eingeschränkt gefühlt '
                   'von den Coronamaßnahmen?'
            },
            'label': {
                1: 'Sehr eingeschränkt',
                2: 'Überhaupt nicht eingeschränkt'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN10Q4': {
            'answers': list(range(1, 5)),
            'questions': {
                4: 'Im Großen und Ganzen halte ich die aktuellen Coronamaßnahmen für:'
            },
            'label': {
                1: 'Zu übertrieben',
                2: 'Müssen viel härter ausfallen'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN10Q5': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                5: 'Haben Sie sich bereits mit Corona infiziert?'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN10Q6': {
            'answers': list(range(1, 5)),
            'questions': {
                6: 'Haben Sie Angst (wieder) an Corona zu erkranken?'
            },
            'label': {
                1: 'Große Angst',
                2: 'Keine Angst'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN10Q7': {
            'answers': list(range(1, 5)),
            'questions': {
                7: 'Haben Sie Angst, dass eine Ihnen nahestehende Person an Corona erkrankt?'
            },
            'label': {
                1: 'Große Angst',
                2: 'Keine Angst'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN10Q8': {
            'answers': [
                [1, 'Keine Zugangsbeschränkungen'],
                [2, '3G'],
                [3, '2G'],
                [4, '2G+'],
                [5, 'Lockdown']
            ],
            'questions': {
                8: 'Was wäre Ihrer Meinung nach aktuell die beste Regel im Umgang mit Corona '
                   'in Bezug auf Freizeitaktivitäten?'
            },
            'widget': widgets.RadioSelect
        },
        'FRAGEN10Q9': {
            'answers': list(range(1, 5)),
            'questions': {
                9: 'Was halten Sie davon eine Pflicht zur Impfung gegen Corona einzuführen?'
            },
            'label': {
                1: 'Sehr befürworten',
                2: 'Entschieden ablehnen'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN10Q10': {
            'answers': list(range(1, 5)),
            'questions': {
                10: 'Wo würden Sie sich politisch einsortieren?'
            },
            'label': {
                1: 'Links',
                2: 'Rechts'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN11': {
            'task': 'Bitte beantworten Sie die folgenden Fragen.'
        },
        'FRAGEN11Q1': {
            'questions': {
                1: 'Wie viel Geld haben Sie monatlich in etwa zur Verfügung (Euro)?'
            },
            'blank': False
        },
        'FRAGEN11Q2': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                2: 'Stehen Sie in einem festen Arbeitsverhältnis mit mehr als 10 Arbeitsstunden in der Woche?'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN11Q3': {
            'answers': [
                [1, 'Weiblich'],
                [2, 'Männlich'],
                [3, 'Divers']
            ],
            'questions': {
                3: 'Geschlecht'
            },
            'widget': widgets.RadioSelect
        },
        'FRAGEN11Q4': {
            'questions': {
                4: 'Alter'
            },
            'blank': False
        },
        'FRAGEN11Q5': {
            'questions': {
                5: 'Wie viele Geschwister haben Sie?'
            },
            'blank': False
        },
        'FRAGEN11Q6': {
            'questions': {
                6: 'Abidurchschnittsnote (1.0 bis 4.0)'
            },
            'blank': True
        },
        'FRAGEN11Q7': {
            'questions': {
                7: 'Letzte Mathenote auf Studium oder Schule (1.0 bis 4.0)'
            },
            'blank': False
        },
        'FRAGEN11Q8': {
            'answers': [
                [1, 'noch nie'],
                [2, '1 bis 2 mal'],
                [3, '3 bis 5 mal'],
                [4, 'öfter']
            ],
            'questions': {
                8: 'Wie häufig haben Sie schon an Experimenten teilgenommen?'
            },
            'widget': widgets.RadioSelect
        },
        'FRAGEN11Q9': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                9: 'Studieren Sie?'
            },
            'widget': widgets.RadioSelectHorizontal
        },
        'FRAGEN11Q10': {
            'questions': {
                10: 'Falls Sie studieren, welches Fach?'
            },
            'blank': True
        },
        'FRAGEN11Q11': {
            'answers': list(range(1, 12)),
            'questions': {
                11: 'Außerdem möchten wir Sie noch nach Ihrer Zufriedenheit mit Ihrem Leben insgesamt fragen. '
                    'Wie zufrieden sind Sie gegenwärtig, alles in allem, mit Ihrem Leben?'
            },
            'label': {
                1: 'ganz und gar unzufrieden',
                2: 'ganz und gar zufrieden'
            },
            'widget': widgets.RadioSelectHorizontal
        },
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Integer Models (Radio Buttons)
    def dataint_radio(name, number):
        return models.IntegerField(
            choices=Constants.forms[name]['answers'],
            label=Constants.forms[name]['questions'][number],
            widget=widgets.RadioSelectHorizontal,
        )

    # Integer Models
    def dataint(name, number):
        return models.IntegerField(
            label=Constants.forms[name]['questions'][number]
        )

    # Integer Models (optional)
    def dataint_blank(name, number):
        return models.IntegerField(
            label=Constants.forms[name]['questions'][number],
            blank=True
        )

    # String Models
    def datastr(name, number):
        return models.StringField(
            label=Constants.forms[name]['questions'][number]
        )

    # String Models (optional)
    def datastr_blank(name, number):
        return models.StringField(
            label=Constants.forms[name]['questions'][number],
            blank=True
        )

    # FRAGEN 1:
    F101 = IntegerField('FRAGEN1Q1', 1)
    F102 = IntegerField('FRAGEN1Q2', 2)

    # FRAGEN 2:
    F201 = IntegerField('FRAGEN2', 1)
    F202 = IntegerField('FRAGEN2', 2)
    F203 = IntegerField('FRAGEN2', 3)

    # FRAGEN 3:
    F301 = IntegerField('FRAGEN3', 1)
    F302 = IntegerField('FRAGEN3', 2)
    F303 = IntegerField('FRAGEN3', 3)

    # FRAGEN 4:
    F401 = IntegerField('FRAGEN4', 1)
    F402 = IntegerField('FRAGEN4', 2)
    F403 = IntegerField('FRAGEN4', 3)
    F404 = IntegerField('FRAGEN4', 4)
    F405 = IntegerField('FRAGEN4', 5)
    F406 = IntegerField('FRAGEN4', 6)
    F407 = IntegerField('FRAGEN4', 7)
    F408 = IntegerField('FRAGEN4', 8)
    F409 = IntegerField('FRAGEN4', 9)
    F410 = IntegerField('FRAGEN4', 10)
    F411 = IntegerField('FRAGEN4', 11)
    F412 = IntegerField('FRAGEN4', 12)
    F413 = IntegerField('FRAGEN4', 13)

    # FRAGEN 5
    F501 = IntegerField('FRAGEN5', 1)
    F502 = IntegerField('FRAGEN5', 2)
    F503 = IntegerField('FRAGEN5', 3)
    F504 = IntegerField('FRAGEN5', 4)
    F505 = IntegerField('FRAGEN5', 5)
    F506 = IntegerField('FRAGEN5', 6)
    F507 = IntegerField('FRAGEN5', 7)
    F508 = IntegerField('FRAGEN5', 8)
    F509 = IntegerField('FRAGEN5', 9)
    F510 = IntegerField('FRAGEN5', 10)

    # FRAGEN 6
    F601 = IntegerField('FRAGEN6', 1)
    F602 = IntegerField('FRAGEN6', 2)
    F603 = IntegerField('FRAGEN6', 3)
    F604 = IntegerField('FRAGEN6', 4)
    F605 = IntegerField('FRAGEN6', 5)
    F606 = IntegerField('FRAGEN6', 6)
    F607 = IntegerField('FRAGEN6', 7)
    F608 = IntegerField('FRAGEN6', 8)
    F609 = IntegerField('FRAGEN6', 9)
    F610 = IntegerField('FRAGEN6', 10)

    # FRAGEN 7
    F701 = StringField('FRAGEN7', 1)
    F702 = StringField('FRAGEN7', 2)

    # FRAGEN 8
    F801 = IntegerField('FRAGEN8Q1', 1)
    F802 = IntegerField('FRAGEN8Q2', 2)

    # FRAGEN 9
    F901 = IntegerField('FRAGEN9Q1_Q3', 1)
    F902 = IntegerField('FRAGEN9Q1_Q3', 2)
    F903 = IntegerField('FRAGEN9Q1_Q3', 3)
    F904 = StringField('FRAGEN9Q4', 4)
    F905 = IntegerField('FRAGEN9Q5_Q14', 5)
    F906 = IntegerField('FRAGEN9Q5_Q14', 6)
    F907 = IntegerField('FRAGEN9Q5_Q14', 7)
    F908 = IntegerField('FRAGEN9Q5_Q14', 8)
    F909 = IntegerField('FRAGEN9Q5_Q14', 9)
    F910 = IntegerField('FRAGEN9Q5_Q14', 10)
    F911 = IntegerField('FRAGEN9Q5_Q14', 11)
    F912 = IntegerField('FRAGEN9Q5_Q14', 12)
    F913 = IntegerField('FRAGEN9Q5_Q14', 13)
    F914 = IntegerField('FRAGEN9Q5_Q14', 14)
    F915 = StringField('FRAGEN9Q15', 15)

    # FRAGEN 10
    F1001 = IntegerField('FRAGEN10Q1', 1)
    F1002 = IntegerField('FRAGEN10Q2', 2)
    F1003 = IntegerField('FRAGEN10Q3', 3)
    F1004 = IntegerField('FRAGEN10Q4', 4)
    F1005 = IntegerField('FRAGEN10Q5', 5)
    F1006 = IntegerField('FRAGEN10Q6', 6)
    F1007 = IntegerField('FRAGEN10Q7', 7)
    F1008 = IntegerField('FRAGEN10Q8', 8)
    F1009 = IntegerField('FRAGEN10Q9', 9)
    F1010 = IntegerField('FRAGEN10Q10', 10)

    # FRAGEN 11
    F1101 = StringField('FRAGEN11Q1', 1)
    F1102 = IntegerField('FRAGEN11Q2', 2)
    F1103 = IntegerField('FRAGEN11Q3', 3)
    F1104 = StringField('FRAGEN11Q4', 4)
    F1105 = StringField('FRAGEN11Q5', 5)
    F1106 = StringField('FRAGEN11Q6', 6)
    F1107 = StringField('FRAGEN11Q7', 7)
    F1108 = IntegerField('FRAGEN11Q8', 8)
    F1109 = IntegerField('FRAGEN11Q9', 9)
    F1110 = StringField('FRAGEN11Q10', 10)
    F1111 = IntegerField('FRAGEN11Q11', 11)
































