from ._builtin import Page, WaitPage


class Introduction(Page):
    pass


class Experiment(Page):
    pass


class DecisionA1(Page):
    pass


class DecisionA2(Page):
    pass


class DecisionB1(Page):
    pass


class DecisionB2(Page):
    pass


class Summary(Page):
    pass


class QuestionsIntroduction(Page):
    pass


class Questions1(Page):

    form_model = 'player'
    form_fields = [
        'CQ101',
        'CQ102'
    ]


class Questions2(Page):

    form_model = 'player'
    form_fields = [
        'CQ201',
        'CQ202'
    ]


class Questions3(Page):

    form_model = 'player'
    form_fields = [
        'CQ301',
        'CQ302'
    ]


page_sequence = [
    Introduction,
    Experiment,
    DecisionA1,
    DecisionA2,
    DecisionB1,
    DecisionB2,
    Summary,
    QuestionsIntroduction,
    Questions1,
    Questions2,
    Questions3
]
