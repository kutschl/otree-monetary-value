from ._builtin import Page, WaitPage


class Introduction(Page):
    def vars_for_template(self):
        self.player.PRIMING_ROLE = self.player.set_priming()


class TextNeutral(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1


class TextRestrict(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2


class TextUseful(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3


class QuestionsNeutral1(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'
    form_fields = [
        'PN01',
        'PN02',
        'PN03'
    ]


class QuestionsRestrict1(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'player'
    form_fields = [
        'PR01',
        'PR02',
        'PR03'
    ]


class QuestionsUseful1(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3

    form_model = 'player'
    form_fields = [
        'PU01',
        'PU02',
        'PU03'
    ]


class QuestionsNeutral2(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'
    form_fields = [
        'PN04',
        'PN05'
    ]


class QuestionsRestrict2(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'player'
    form_fields = [
        'PR04',
        'PR05'
    ]


class QuestionsUseful2(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3

    form_model = 'player'
    form_fields = [
        'PU04',
        'PU05'
    ]


page_sequence = [
    Introduction,
    TextNeutral,
    TextRestrict,
    TextUseful,
    QuestionsNeutral1,
    QuestionsNeutral2,
    QuestionsRestrict1,
    QuestionsRestrict2,
    QuestionsUseful1,
    QuestionsUseful2
]
