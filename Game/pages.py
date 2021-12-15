from ._builtin import Page, WaitPage


class PrimingStart(Page):
    def vars_for_template(self):
        self.player.PRIMING_ROLE = self.player.set_priming()


class PrimingNeutralText(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1


class PrimingRestrictText(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2


class PrimingUsefulText(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3


class PrimingNeutralQuestions(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'
    form_fields = [
        'PN01',
        'PN02',
        'PN03',
        'PN04',
        'PN05',
    ]


class PrimingRestrictQuestions(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'player'
    form_fields = [
        'PR01',
        'PR02',
        'PR03',
        'PR04',
        'PR05',
    ]


class PrimingUsefulQuestions(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3

    form_model = 'player'
    form_fields = [
        'PU01',
        'PU02',
        'PU03',
        'PU04',
        'PU05',
    ]


class ControlQuestions1(Page):

    form_model = 'player'
    form_fields = [
        'C101',
        'C102'
    ]


class ControlQuestions2(Page):

    form_model = 'player'
    form_fields = [
        'C201',
        'C202'
    ]


class ControlQuestions3(Page):

    form_model = 'player'
    form_fields = [
        'C301',
        'C302'
    ]


class FragebogenStart(Page):
    pass


class Fragebogen1(Page):

    form_model = 'player'
    form_fields = [
        'F101',
        'F102'
    ]


class Fragebogen2(Page):

    form_model = 'player'
    form_fields = [
        'F201',
        'F202',
        'F203'
    ]


class Fragebogen3(Page):

    form_model = 'player'
    form_fields = [
        'F301',
        'F302',
        'F303'
    ]


class Fragebogen4(Page):

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


class Fragebogen5(Page):

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


class Fragebogen6(Page):

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


class Fragebogen7(Page):

    form_model = 'player'
    form_fields = [
        'F701',
        'F702'
    ]


class Fragebogen8(Page):

    form_model = 'player'
    form_fields = [
        'F801',
        'F802'
    ]


class Fragebogen9(Page):

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


class Fragebogen10(Page):

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


class Fragebogen11(Page):

    form_model = 'player'
    form_fields = [
        'F1101_EINKOMMEN',
        'F1102_ARBEIT',
        'F1103_GESCHLECHT',
        'F1104_ALTER',
        'F1105_GESCHWISTER',
        'F1106_ABINOTE',
        'F1107_MATHENOTE',
        'F1108_EXPERIMENTE',
        'F1109_STUDIUM',
        'F1110_STUDIENFACH',
        'F1111_ZUFRIEDENHEIT'
    ]


page_sequence = [
    PrimingStart,
    #PrimingNeutralText,
    #PrimingRestrictText,
    #PrimingUsefulText,
    #PrimingNeutralQuestions,
    #PrimingUsefulQuestions,
    #PrimingRestrictQuestions,
    #ControlQuestions1,
    #ControlQuestions2,
    #ControlQuestions3,
    FragebogenStart,
    #Fragebogen1,
    #Fragebogen2,
    #Fragebogen3,
    #Fragebogen4,
    #Fragebogen5,
    #Fragebogen6,
    #Fragebogen7,
    #Fragebogen8,
    #Fragebogen9,
    Fragebogen10,
    Fragebogen11,
]
