# scripts/delete_all_questions.py
import json
from Statistics.models import Player



def run():
    # read file
    playerJSONList = json.load(open('/Users/seanoneill/Code/HockeyMonday/Statistics/players.json', 'r'))
    for playerJSON in playerJSONList:
        print(int(playerJSON["Games Played"]))
        newPlayer = Player( name = playerJSON['Player'], games_played = int(playerJSON['Games Played']),
        match_points = int(playerJSON['Match Points']), goals = int(playerJSON['Goals']),
        assists = int(playerJSON['Assists']), points =  int(playerJSON['Points']), saves = int(playerJSON['Saves']), current_streak = int(playerJSON['Winning Streak']) ,
        goals_in_a_game = int(playerJSON['Goals in a Game']) , assists_in_a_game = int(playerJSON['Assists in a Game']) , points_in_a_game =  int(playerJSON['Points in a Game']))
        newPlayer.save()
    



