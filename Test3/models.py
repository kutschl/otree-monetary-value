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
    name_in_url = 'Test3'
    players_per_group = None
    num_rounds = 1

    participation_fee = c(0)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    RANDOM = models.IntegerField()




















