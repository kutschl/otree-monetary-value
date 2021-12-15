import random

from ._builtin import Page, WaitPage


class Start1(Page):
    def is_displayed(self):
        return self.player.participant.vars['shuffle'][self.round_number - 1] == 1

    def vars_for_template(self):
        if self.player.participant.vars['shuffle'][self.round_number - 1] == 1:
            print(True, self.round_number)


class Start2(Page):
    def is_displayed(self):
        return self.player.participant.vars['shuffle'][self.round_number - 1] == 2

    def vars_for_template(self):
        if self.player.participant.vars['shuffle'][self.round_number - 1] == 2:
            print(True, self.round_number)


class Start3(Page):
    def is_displayed(self):
        return self.player.participant.vars['shuffle'][self.round_number - 1] == 3

    def vars_for_template(self):
        if self.player.participant.vars['shuffle'][self.round_number - 1] == 3:
            print(True, self.round_number)


class Start4(Page):
    def is_displayed(self):
        return self.player.participant.vars['shuffle'][self.round_number - 1] == 4

    def vars_for_template(self):
        if self.player.participant.vars['shuffle'][self.round_number - 1] == 4:
            print(True, self.round_number)


page_sequence = [
    Start1,
    Start2,
    Start3,
    Start4
]
