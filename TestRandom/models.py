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

import random
import itertools
import json

doc = ""


class Constants(BaseConstants):
    name_in_url = 'TestRandom'
    players_per_group = None
    num_rounds = 4

    participation_fee = c(0)


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                round_numbers = list(range(2, Constants.num_rounds + 1))
                random.shuffle(round_numbers)
                round_numbers.insert(0, 1)
                print(round_numbers)
                p.participant.vars['shuffle'] = round_numbers


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


















