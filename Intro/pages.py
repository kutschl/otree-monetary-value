from ._builtin import Page, WaitPage


class Introduction(Page):
    def vars_for_template(self):
        self.player.payoff = 0
        self.participant.vars['payoff'] = 0


class EmailValidation(Page):

    form_model = 'player'
    form_fields = [
        'EMAIL_VALID'
    ]


class PaymentInfo(Page):

    form_model = 'player'
    form_fields = [
        'VORNAME',
        'NACHNAME',
        'STRASSE',
        'HAUSNUMMER',
        'PLZ',
        'ORT',
        'IBAN',
        'BIC'
    ]


page_sequence = [
    Introduction,
    EmailValidation,
    PaymentInfo
]
