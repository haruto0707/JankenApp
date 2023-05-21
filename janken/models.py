from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUser(AbstractUser):
    play_num = models.IntegerField(default=0)
    win_num = models.IntegerField(default=0)
    lose_num = models.IntegerField(default=0)
    draw_num = models.IntegerField(default=0)
    win_rate = models.FloatField(default=0.0)

    stone_num = models.IntegerField(default=0)
    scissors_num = models.IntegerField(default=0)
    paper_num = models.IntegerField(default=0)

    image = models.ImageField(upload_to='img/')

    def play(self, player_hand, com_hand):
        if player_hand == com_hand:
            result = 'draw'
            self.draw_num += 1
        elif player_hand == 'stone' and com_hand == 'scissors' or player_hand == 'scissors' and com_hand == 'paper' or player_hand == 'paper' and com_hand == 'stone':
            result = 'win'
            self.win_num += 1
        else:
            self.lose_num += 1
            result = 'lose'

        if player_hand == 'stone':
            self.stone_num += 1
        elif player_hand == 'scissors':
            self.scissors_num += 1
        else:
            self.paper_num += 1

        self.play_num = self.win_num + self.lose_num + self.draw_num
        self.win_rate = self.win_num / self.play_num * 100

        return result
