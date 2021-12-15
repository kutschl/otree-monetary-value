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

doc = ""


class Constants(BaseConstants):
    name_in_url = 'Game'
    players_per_group = 3
    num_rounds = 1

    fee_participation = c(0)
    fee_questionnaire = c(10)

    # todo: Kontaktdaten einfügen
    contact = {
        'phone': None,
        'email': None
    }

    data = {
        'C1': {
            'task': 'Angenommen Sie hätten die Tabelle in einer Entscheidungssituation so ausgefüllt wie in der '
                    ' Abbildung dargestellt. Zudem ist diese Entscheidungssituation für Sie auszahlungsrelevant.'
        },
        'C101': {
            'answers': [
                [1, 'Kommt drauf an, wie die Investitionsgelegenheit ausgelost wird.'],
                [2, '5€'],
                [3, '2.5€']
            ],
            'questions': {
                1: 'a) Wie hoch ist Ihre Auszahlung, wenn die <b>letzte </b> Zeile der Tabelle ausgelost wurde?',
            },
            'solution': 2
        },
        'C102': {
            'answers': [
                [1, 'Kommt drauf an, wie die Investitionsgelegenheit ausgelost wird.'],
                [2, '5€'],
                [3, '2.5€']
            ],
            'questions': {
                1: 'b) Wie hoch ist Ihre Auszahlung, wenn die <b>zweite</b> Zeile der Tabelle ausgelost wurde?'
            },
            'solution': 1
        },
        'C2': {
            'task': 'Angenommen Sie hätten die Tabelle in einer Entscheidungssituation so ausgefüllt wie in '
                    'der Abbildung dargestellt. Zudem ist diese Entscheidungssituation für Sie auszahlungsrelevant.'
        },
        'C201': {
            'answers': [
                [1, 'Wenn die 3. Zeile der unteren Tabelle ausgelost wurde (1€ Kosten zum Aufheben der Vorauswahl)'],
                [2, 'Wenn ein Betrag von kleiner oder gleich 2€ als Kosten ausgelost wurde.'],
                [3, 'Beide Antworten sind richtig.']
            ],
            'questions': {
                1: 'a) Wann können Sie die obige Entscheidung selbst treffen?',
            },
            'solution': 3
        },
        'C202': {
            'answers': [
                [1, '5€'],
                [2, '4€'],
                [3, '1€']
            ],
            'questions': {
                1: 'b) Nehmen Sie an, die <b>dritte</b> Zeile der unteren Tabelle wurde ausgelost, Sie konnten die '
                   'Entscheidung oben also wieder frei treffen (zu Kosten von 1€). Sie haben sich für die '
                   'Investitionsgelegenheit entschieden und erhalten daraufhin 5€ aus der Investitionsgelegenheit. '
                   'Wie hoch ist Ihre Auszahlung?'
            },
            'solution': 2
        },
        'C3': {
            'task': 'Angenommen Sie hätten die Tabelle in einer Entscheidungssituation so ausgefüllt wie in '
                    'der Abbildung dargestellt. Zudem ist diese Entscheidungssituation für Sie auszahlungsrelevant.'
        },
        'C301': {
            'answers': [
                [1, '2€'],
                [2, '5€'],
                [3, '3€'],
                [4, 'Kommt darauf an wie die Investitionsgelegenheit ausfällt.']
            ],
            'questions': {
                1: 'c) Wie hoch ist Ihre Auszahlung, wenn in der unteren Tabelle die <b>letzte</b> Zeile ausgelost '
                   'wurde?',
            },
            'solution': 1
        },
        'C302': {
            'answers': [
                [1, 'Die Vorauswahl wird in jedem Fall auszahlungsrelevant sein.'],
                [2, 'Die obige Entscheidung kann wieder frei getroffen werden.'],
                [3, 'Sie sind bereit mindestens 1€ zu bezahlen, um die Vorauswahl aufzuheben.']
            ],
            'questions': {
                1: 'd) Nehmen Sie an, Sie hätten in <b>jeder</b> Zeile in der unteren Tabelle "nein" angekreuzt. '
                   'Was bedeutet das?'
            },
            'solution': 1
        },
        'PN1': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                1: 'Sind/Waren Sie Student(in) an der Universität Bonn?',
                2: 'Wussten Sie, dass die Universität Bonn 2018 200-jähriges Jubiläum feierte?',
                3: 'Ist Ihnen die Exzellenzinitiative bekannt?'
            },
        },
        'PN2': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Es ist wichtig die Geschichte einer Universität zu kennen um deren Gegenwart und Zukunft '
                   'zu beurteilen.',
                2: 'Es sollte mehr Wert darauf gelegt werden die Geschichte einer Universität an Studierende '
                   'und MitarbeiterInnen zu vermitteln'
            },
            'task': 'Wie sehr stimmen Sie den folgenden 2 Aussagen zu:',
            'label': {
                1: 'Stimme überhaupt nicht zu',
                2: 'Stimme voll und ganz zu'
            }
        },
        'PU1': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                1: 'Gehören Sie selbst zu einer Risikogruppe?',
                2: 'Haben Sie regelmäßig Kontakt zu Personen, die zu einer Risikogruppe gehören?',
                3: 'Kennen Sie Personen, die an COVID-19 erkrankt sind?'
            }
        },
        'PU2': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Während der ersten Corona Welle Sorgen habe ich mir große Sorgen gemacht über meine eigene '
                   'Gesundheit und/oder über die Gesundheit meiner Freunde und/oder meiner Familie?',
                2: 'Während der ersten Corona Welle hatte ich Angst davor, dass das Gesundheitssystem '
                   'zusammenbrechen könnte und somit sowohl Corona-Erkrankte als auch andere Notfälle nicht '
                   'mehr ausreichend versorgt werden könnten.'
            },
            'task': 'Wie sehr stimmen Sie den folgenden 2 Aussagen zu:',
            'label': {
                1: 'Stimme überhaupt nicht zu',
                2: 'Stimme voll und ganz zu'
            }
        },
        'PR1': {
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
            }
        },
        'PR2': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Ich oder mir nahestehende Personen haben durch die Maßnahmen der Pandemie in der ersten '
                   'Welle mentale Beschwerden erlebt, wie zum Beispiel Einsamkeit oder depressive Zustände?',
                2: 'Ich habe mir während der ersten Corona Welle große Sorgen gemacht über meine eigene '
                   'berufliche Zukunft und/oder über die berufliche Zukunft meiner Freunde bzw. meiner Familie?'
            },
            'task': 'Wie sehr stimmen Sie den folgenden 2 Aussagen zu: ',
            'label': {
                1: 'Stimme überhaupt nicht zu',
                2: 'Stimme voll und ganz zu'
            }
        },
        'F1': {
            'task': 'Bitte beantworten Sie die folgenden Fragen',
        },
        'F1_Q1': {
            'answers': list(range(1, 12)),
            'questions': {
                1: 'Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder '
                   'versuchen Sie, Risiken zu vermeiden?'
            },
            'label': {
                1: 'Gar nicht risikobereit',
                2: 'Sehr risikobereit'
            }
        },
        'F1_Q2': {
            'answers': list(range(1, 12)),
            'questions': {
                2: 'Wie hoch ist Ihre Bereitschaft, auf etwas zu verzichten, zm in Zukunft darauf zu profitieren, '
                   'wenn es um finanzielle Entscheidungen geht?',
            },
            'label': {
                1: 'Keine Bereitschaft',
                2: 'Sehr hohe Bereitschaft'
            }
        },
        'F2': {
            'answers': list(range(1, 12)),
            'questions': {
                1: 'Wie sehr wären Sie bereit, jemanden zu bestrafen, der <b>Sie</b> unfair behandelt, selbst wenn'
                   'dies für Sie negative Konsequenzen hat? ',
                2: 'Wie sehr wären Sie bereit, jemanden zu bestrafen, der <b>andere</b> unfair behandelt, selbst wenn'
                   'dies für Sie Kosten verursachen würde?',
                3: 'Wie sehr wären Sie bereit, für einen guten Zweck zu geben, ohne etwas als Gegenleitung zu erwarten?'
            },
            'task': 'Bitte beantworten Sie die folgenden Fragen',
            'label': {
                1: 'Keine Bereitschaft',
                2: 'Sehr hohe Bereitschaft'
            }
        },
        'F3': {
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
            }
        },
        'F4': {
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
            }
        },
        'F5': {
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
            }
        },
        'F6': {
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
            }
        },
        'F7': {
            'questions': {
                1: 'Um was ging es in diesem Experiment Ihrer Meinung nach?',
                2: 'Bitte nennen Sie Gründe für Ihre Entscheidung in den Situationen mit Vorauswahl.'
            },
            'task': 'Bitte beantworten Sie die folgenden Fragen in Stichpunkten.'
        },
        'F8': {
            'task': 'In den folgenden Fragen geht es um den Block an Entscheidungssituationen, in denen Ihre '
                    'Entscheidung durch eine Vorauswahl eingeschränkt wurde.'
        },
        'F8_Q1': {
            'answers': list(range(1, 6)),
            'questions': {
                1: 'Haben Sie sich in den Entscheidungssituationen mit Vorauswahl eingeschränkt gefühlt?'
            },
            'label': {
                1: 'Nein, gar nicht',
                2: 'Ja, sehr'
            }
        },
        'F8_Q2': {
            'answers': [
                [1, 'nicht oder kaum gestört'],
                [2, 'prinzipiell gestört'],
                [3, 'nur gestört, wenn meine bevorzugte Wahl nicht zur Verfügung stand']
            ],
            'questions': {
                2: 'Die Vorauswahl hat mich ...'
            }
        },
        'F9': {
            'task': 'In den folgenden Fragen geht es um den Block an Entscheidungssituationen, in denen Ihre '
                    'Entscheidung durch eine Vorauswahl eingeschränkt wurde.'
        },
        'F9_Q1toQ4': {
            'task': 'Ich habe die Vorauswahl wahrgenommen als ...'
        },
        'F9_Q1toQ3': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                1: 'Eingriff in meine Autonomie und Entscheidungsfreiheit',
                2: 'Einschränkung meines Handlungsspielraumes für die spezifischen Situationen',
                3: 'Gar nicht/kaum wahrgenommen'
            }
        },
        'F9_Q4': {
            'questions': {
                4: 'Sonstiges'
            }
        },
        'F9_Q5toQ15': {
            'task': 'Ich welchen der folgenden Situationen kann es aus Ihrer persönlichen Sicht gerechtfertigt '
                    'sein, wenn der Staat individuellen Handlungsspielraum einschränkt?'
        },
        'F9_Q5to14': {
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
            }
        },
        'F9_Q15': {
            'questions': {
                15: 'Sonstiges'
            }
        },
        'F10': {
            'task': 'Bitte beantworten Sie die folgenden Fragen.'
        },
        'F10_Q1': {
            'answers': list(range(1, 5)),
            'questions': {
                1: 'Wie viel Vertrauen haben Sie generell in die Regierung / in die Politik die richtigen Maßnahmen '
                   'in der Reaktion auf eine Krisensituation zu erlassen?'
            },
            'label': {
                1: 'Überhaupt kein Vertrauen',
                2: 'Volles Vertrauen'
            }
        },
        'F10_Q2': {
            'answers': list(range(1, 5)),
            'questions': {
                2: 'Wie sehr wird Ihr Alltag momentan negativ von Corona beeinflusst?'
            },
            'label': {
                1: 'Überhaupt nicht beeinträchtigt',
                2: 'Sehr stark beeinträchtigt'
            }
        },
        'F10_Q3': {
            'answers': list(range(1, 5)),
            'questions': {
                3: 'Wie sehr haben Sie sich generell über die gesamte Zeit der Pandemie hinweg eingeschränkt gefühlt '
                   'von den Coronamaßnahmen?'
            },
            'label': {
                1: 'Sehr eingeschränkt',
                2: 'Überhaupt nicht eingeschränkt'
            }
        },
        'F10_Q4': {
            'answers': list(range(1, 5)),
            'questions': {
                4: 'Im Großen und Ganzen halte ich die aktuellen Coronamaßnahmen für:'
            },
            'label': {
                1: 'Zu übertrieben',
                2: 'Müssen viel härter ausfallen'
            }
        },
        'F10_Q5': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                5: 'Haben Sie sich bereits mit Corona infiziert?'
            }
        },
        'F10_Q6': {
            'answers': list(range(1, 5)),
            'questions': {
                6: 'Haben Sie Angst (wieder) an Corona zu erkranken?'
            },
            'label': {
                1: 'Große Angst',
                2: 'Keine Angst'
            }
        },
        'F10_Q7': {
            'answers': list(range(1, 5)),
            'questions': {
                7: 'Haben Sie Angst, dass eine Ihnen nahestehende Person an Corona erkrankt?'
            },
            'label': {
                1: 'Große Angst',
                2: 'Keine Angst'
            }
        },
        'F10_Q8': {
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
        },
        'F10_Q9': {
            'answers': list(range(1, 5)),
            'questions': {
                9: 'Was halten Sie davon eine Pflicht zur Impfung gegen Corona einzuführen?'
            },
            'label': {
                1: 'Sehr befürworten',
                2: 'Entschieden ablehnen'
            }
        },
        'F10_Q10': {
            'answers': list(range(1, 5)),
            'questions': {
                10: 'Wo würden Sie sich politisch einsortieren?'
            },
            'label': {
                1: 'Links',
                2: 'Rechts'
            }
        },
        'F11': {
            'task': 'Bitte beantworten Sie die folgenden Fragen.'
        },
        'F11_Q1': {
            'questions': {
                1: 'Wie viel Geld haben Sie monatlich in etwa zur Verfügung (Euro)?'
            },
        },
        'F11_Q2': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                2: 'Stehen Sie in einem festen Arbeitsverhältnis mit mehr als 10 Arbeitsstunden in der Woche?'
            }
        },
        'F11_Q3': {
            'answers': [
                [1, 'Weiblich'],
                [2, 'Männlich'],
                [3, 'Divers']
            ],
            'questions': {
                3: 'Geschlecht'
            }
        },
        'F11_Q4': {
            'questions': {
                4: 'Alter'
            }
        },
        'F11_Q5': {
            'questions': {
                5: 'Wie viele Geschwister haben Sie?'
            }
        },
        'F11_Q6': {
            'questions': {
                6: 'Abidurchschnittsnote (1.0 bis 4.0)'
            }
        },
        'F11_Q7': {
            'questions': {
                7: 'Letzte Mathenote auf Studium oder Schule (1.0 bis 4.0)'
            }
        },
        'F11_Q8': {
            'answers': [
                [1, 'noch nie'],
                [2, '1 bis 2 mal'],
                [3, '3 bis 5 mal'],
                [4, 'öfter']
            ],
            'questions': {
                8: 'Wie häufig haben Sie schon an Experimenten teilgenommen?'
            }
        },
        'F11_Q9': {
            'answers': [
                [1, 'Ja'],
                [2, 'Nein']
            ],
            'questions': {
                9: 'Studieren Sie?'
            }
        },
        'F11_Q10': {
            'questions': {
                10: 'Falls Sie studieren, welches Fach?'
            }
        },
        'F11_Q11': {
            'answers': list(range(1, 12)),
            'questions': {
                11: 'Außerdem möchten wir Sie noch nach Ihrer Zufriedenheit mit Ihrem Leben insgesamt fragen. '
                    'Wie zufrieden sind Sie gegenwärtig, alles in allem, mit Ihrem Leben?'
            },
            'label': {
                1: 'ganz und gar unzufrieden',
                2: 'ganz und gar zufrieden'
            }
        },
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Set Priming
    def set_priming(self):
        if self.id_in_group == 1:
            return 'NEUTRAL'
        if self.id_in_group == 2:
            return 'RESTRICT'
        else:
            return 'USEFUL'

    # Integer Models (Radio Buttons)
    def dataint_radio(name, number):
        return models.IntegerField(
            choices=Constants.data[name]['answers'],
            label=Constants.data[name]['questions'][number],
            widget=widgets.RadioSelectHorizontal,
        )

    # Integer Models
    def dataint(name, number):
        return models.IntegerField(
            label=Constants.data[name]['questions'][number]
        )

    # Integer Models (optional)
    def dataint_blank(name, number):
        return models.IntegerField(
            label=Constants.data[name]['questions'][number],
            blank=True
        )

    # String Models
    def datastr(name, number):
        return models.StringField(
            label=Constants.data[name]['questions'][number]
        )

    # String Models (optional)
    def datastr_blank(name, number):
        return models.StringField(
            label=Constants.data[name]['questions'][number],
            blank=True
        )

    # PRIMING ROLE
    PRIMING_ROLE = models.StringField()

    # CONTROL QUESTIONS
    C101 = dataint_radio('C101', 1)
    C102 = dataint_radio('C102', 1)
    C201 = dataint_radio('C201', 1)
    C202 = dataint_radio('C202', 1)
    C301 = dataint_radio('C301', 1)
    C302 = dataint_radio('C302', 1)

    # PRIMING QUESTIONS NEUTRAL
    PN01 = dataint_radio('PN1', 1)
    PN02 = dataint_radio('PN1', 2)
    PN03 = dataint_radio('PN1', 3)
    PN04 = dataint_radio('PN2', 1)
    PN05 = dataint_radio('PN2', 2)

    # PRIMING QUESTIONS USEFUL
    PU01 = dataint_radio('PU1', 1)
    PU02 = dataint_radio('PU1', 2)
    PU03 = dataint_radio('PU1', 3)
    PU04 = dataint_radio('PU2', 1)
    PU05 = dataint_radio('PU2', 2)

    # PRIMING QUESTIONS RESTRICT
    PR01 = dataint_radio('PR1', 1)
    PR02 = dataint_radio('PR1', 2)
    PR03 = dataint_radio('PR1', 3)
    PR04 = dataint_radio('PR2', 1)
    PR05 = dataint_radio('PR2', 2)

    # FRAGEN 1:
    F101 = dataint_radio('F1_Q1', 1)
    F102 = dataint_radio('F1_Q2', 2)

    # FRAGEN 2:
    F201 = dataint_radio('F2', 1)
    F202 = dataint_radio('F2', 2)
    F203 = dataint_radio('F2', 3)

    # FRAGEN 3:
    F301 = dataint_radio('F3', 1)
    F302 = dataint_radio('F3', 2)
    F303 = dataint_radio('F3', 3)

    # FRAGEN 4:
    F401 = dataint_radio('F4', 1)
    F402 = dataint_radio('F4', 2)
    F403 = dataint_radio('F4', 3)
    F404 = dataint_radio('F4', 4)
    F405 = dataint_radio('F4', 5)
    F406 = dataint_radio('F4', 6)
    F407 = dataint_radio('F4', 7)
    F408 = dataint_radio('F4', 8)
    F409 = dataint_radio('F4', 9)
    F410 = dataint_radio('F4', 10)
    F411 = dataint_radio('F4', 11)
    F412 = dataint_radio('F4', 12)
    F413 = dataint_radio('F4', 13)

    # FRAGEN 5
    F501 = dataint_radio('F5', 1)
    F502 = dataint_radio('F5', 2)
    F503 = dataint_radio('F5', 3)
    F504 = dataint_radio('F5', 4)
    F505 = dataint_radio('F5', 5)
    F506 = dataint_radio('F5', 6)
    F507 = dataint_radio('F5', 7)
    F508 = dataint_radio('F5', 8)
    F509 = dataint_radio('F5', 9)
    F510 = dataint_radio('F5', 10)

    # FRAGEN 6
    F601 = dataint_radio('F5', 1)
    F602 = dataint_radio('F6', 2)
    F603 = dataint_radio('F6', 3)
    F604 = dataint_radio('F6', 4)
    F605 = dataint_radio('F6', 5)
    F606 = dataint_radio('F6', 6)
    F607 = dataint_radio('F6', 7)
    F608 = dataint_radio('F6', 8)
    F609 = dataint_radio('F6', 9)
    F610 = dataint_radio('F6', 10)

    # FRAGEN 7
    F701 = datastr('F7', 1)
    F702 = datastr('F7', 2)

    # FRAGEN 8
    F801 = dataint_radio('F8_Q1', 1)
    F802 = dataint_radio('F8_Q2', 2)

    # FRAGEN 9
    F901 = dataint_radio('F9_Q1toQ3', 1)
    F902 = dataint_radio('F9_Q1toQ3', 2)
    F903 = dataint_radio('F9_Q1toQ3', 3)
    F904 = datastr_blank('F9_Q4', 4)
    F905 = dataint_radio('F9_Q5to14', 5)
    F906 = dataint_radio('F9_Q5to14', 6)
    F907 = dataint_radio('F9_Q5to14', 7)
    F908 = dataint_radio('F9_Q5to14', 8)
    F909 = dataint_radio('F9_Q5to14', 9)
    F910 = dataint_radio('F9_Q5to14', 10)
    F911 = dataint_radio('F9_Q5to14', 11)
    F912 = dataint_radio('F9_Q5to14', 12)
    F913 = dataint_radio('F9_Q5to14', 13)
    F914 = dataint_radio('F9_Q5to14', 14)
    F915 = datastr_blank('F9_Q15', 15)

    # FRAGEN 10
    F1001 = dataint_radio('F10_Q1', 1)
    F1002 = dataint_radio('F10_Q2', 2)
    F1003 = dataint_radio('F10_Q3', 3)
    F1004 = dataint_radio('F10_Q4', 4)
    F1005 = dataint_radio('F10_Q5', 5)
    F1006 = dataint_radio('F10_Q6', 6)
    F1007 = dataint_radio('F10_Q7', 7)
    F1008 = dataint_radio('F10_Q8', 8)
    F1009 = dataint_radio('F10_Q9', 9)
    F1010 = dataint_radio('F10_Q10', 10)

    # FRAGEN 11
    F1101_EINKOMMEN = dataint('F11_Q1', 1)
    F1102_ARBEIT = dataint_radio('F11_Q2', 2)
    F1103_GESCHLECHT = dataint_radio('F11_Q3', 3)
    F1104_ALTER = dataint('F11_Q4', 4)
    F1105_GESCHWISTER = dataint('F11_Q5', 5)
    F1106_ABINOTE = dataint_blank('F11_Q6', 6)
    F1107_MATHENOTE = dataint_blank('F11_Q7', 7)
    F1108_EXPERIMENTE = dataint_radio('F11_Q8', 8)
    F1109_STUDIUM = dataint_radio('F11_Q9', 9)
    F1110_STUDIENFACH = datastr_blank('F11_Q10', 10)
    F1111_ZUFRIEDENHEIT = dataint_radio('F11_Q11', 11)
































