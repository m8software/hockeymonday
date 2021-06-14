from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=75)
    games_played = models.IntegerField()
    match_points = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    points = models.IntegerField()
    saves = models.IntegerField()
    #losses could be negative, wins postive
    current_streak = models.IntegerField()
    goals_in_a_game = models.IntegerField()
    assists_in_a_game = models.IntegerField()
    points_in_a_game = models.IntegerField()



    def __str__(self):
        return  self.name

class Game(models.Model):
    date_time_start = models.DateTimeField()
    date_time_end = models.DateTimeField(null=True, blank=True)
    winScore = models.IntegerField()
    loseScore = models.IntegerField()
    team_one = models.ManyToManyField(Player, related_name='team_1', null=True, blank=True,)
    team_two = models.ManyToManyField(Player, related_name='team_2', null=True, blank=True,)

    def __str__(self):
        return  self.date_time_start.strftime('%Y-%m-%d %H:%M')

class Goal(models.Model):
    date_time = models.DateTimeField(primary_key=True,)
    scorer = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='scorer_player'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='game_in'
    )
    goalie = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='goalie_player'
        
    )
    assist = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='assist_player'
        
    )

    def __str__(self):
        return  self.scorer.name + " " + self.date_time.strftime('%Y-%m-%d %H:%M')