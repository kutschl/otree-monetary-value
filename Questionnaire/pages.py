from ._builtin import Page, WaitPage


class Introduction(Page):
    pass


class Fragen1(Page):

    form_model = 'player'
    form_fields = [
        'F101',
        'F102'
    ]


class Fragen2(Page):

    form_model = 'player'
    form_fields = [
        'F201',
        'F202',
        'F203'
    ]


class Fragen3(Page):

    form_model = 'player'
    form_fields = [
        'F301',
        'F302',
        'F303'
    ]


class Fragen4(Page):

    form_model = 'player'
    form_fields = [
        'F401',
        'F402',
        'F403',
        'F404',
        'F405',
        'F406',
        'F407',
        'F408',
        'F409',
        'F410',
        'F411',
        'F412',
        'F413'
    ]


class Fragen5(Page):

    form_model = 'player'
    form_fields = [
        'F501',
        'F502',
        'F503',
        'F504',
        'F505',
        'F506',
        'F507',
        'F508',
        'F509',
        'F510'
    ]


class Fragen6(Page):

    form_model = 'player'
    form_fields = [
        'F601',
        'F602',
        'F603',
        'F604',
        'F605',
        'F606',
        'F607',
        'F608',
        'F609',
        'F610'
    ]


class Fragen7(Page):

    form_model = 'player'
    form_fields = [
        'F701',
        'F702'
    ]


class Fragen8(Page):

    form_model = 'player'
    form_fields = [
        'F801',
        'F802'
    ]


class Fragen9(Page):

    form_model = 'player'
    form_fields = [
        'F901',
        'F902',
        'F903',
        'F904',
        'F905',
        'F906',
        'F907',
        'F908',
        'F909',
        'F910',
        'F911',
        'F912',
        'F913',
        'F914',
        'F915'
    ]


class Fragen10(Page):

    form_model = 'player'
    form_fields = [
        'F1001',
        'F1002',
        'F1003',
        'F1004',
        'F1005',
        'F1006',
        'F1007',
        'F1008',
        'F1009',
        'F1010'
    ]


class Fragen11(Page):

    form_model = 'player'
    form_fields = [
        'F1101',
        'F1102',
        'F1103',
        'F1104',
        'F1105',
        'F1106',
        'F1107',
        'F1108',
        'F1109',
        'F1110',
        'F1111'
    ]


page_sequence = [
    Introduction,
    Fragen1,
    Fragen2,
    Fragen3,
    Fragen4,
    Fragen5,
    Fragen6,
    Fragen7,
    Fragen8,
    Fragen9,
    Fragen10,
    Fragen11,
]
