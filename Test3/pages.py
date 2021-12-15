import random

from ._builtin import Page, WaitPage


class Start3(Page):
    def vars_for_template(self):
        self.player.RANDOM = random.randint(1, 3)

    def app_after_this_page(self, upcoming_apps):
        if self.player.RANDOM == 1:
            return 'Test1'
        if self.player.RANDOM == 2:
            return 'Test2'
        else:
            return 'Test3'

    form_model = 'player'
    form_fields = [
        'RANDOM'
    ]


page_sequence = [
    Start3
]
