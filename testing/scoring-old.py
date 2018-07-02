import constants as c
import os
from datetime import datetime as dt
from team_check import team_count_is_good as check
import time

#countries, iso 3166-2, and reversed (k,v)
country_to_code = {'Egypt': 'EG', 'Morocco': 'MA', 'Nigeria': 'NG', 'Senegal': 'SN', 'Tunisia': 'TN', 'Australia': 'AU', 'Iran': 'IR', 'Japan': 'JP', 'South Korea': 'KR', 'Saudi Arabia': 'SA', 'Belgium': 'BE', 'Croatia': 'HR', 'Denmark': 'DK', 'England': 'GB', 'France': 'FR', 'Germany': 'DE', 'Iceland': 'IS', 'Poland': 'PL', 'Portugal': 'PT', 'Russia': 'RU', 'Serbia': 'RS', 'Spain': 'ES', 'Sweden': 'SE', 'Switzerland': 'CH', 'Costa Rica': 'CR', 'Mexico': 'MX', 'Panama': 'PA', 'Argentina': 'AR', 'Brazil': 'BR', 'Colombia': 'CO', 'Peru': 'PE', 'Uruguay': 'UY'}
code_to_country = {v:k for k,v in country_to_code.items()}

#seeds dict
with open('teams/team-seeds.txt') as f:
    seeds = {x.rstrip():i+1 for i, x in enumerate(f)}

#true if a is higher seed than b
def is_higher_seed(a, b):
    s = len(seeds)
    return ((s-seeds[a])-(s-seeds[b])) > 0

#parsing the string for getting the teams and scores for a game
def get_scores(w, l):
    w_name = code_to_country[w[:2]]
    w_score = int(w[2:])
    l_name = code_to_country[l[:2]]
    l_score = int(l[2:])
    return w_name, w_score, l_name, l_score

#probably some easy way using * opperator but literally repeats string s n times
def repeat(s, n):
    return ''.join([s for i in range(n)])

#pretty dictionary, makes sure that all entries are evenly spaced to display kv pairs
def pdict(d, div='    '):
    m = max([len(x) for x in d])
    return '\n'.join([str(x) + repeat(' ', m - len(str(x))) + str(div) + str(d[x]) for x in d])

# print('\n'.join([country_to_code[x] + '    ' + x for x in country_to_code]))

#categories to look for
team_goals_scored = {x: 0 for x in country_to_code.keys()}
team_goals_allowed = {x: 0 for x in country_to_code.keys()}
team_win_loss_points = {x: 0 for x in country_to_code.keys()}
# print(team_goals_scored)

#giving teams points for winngin
with open('team-scores.txt') as scores:
    for line in scores:
        #ignore empty and commented lines
        if len(line) > 0 and line[0] != '#' and line != '\n':
            line = line.replace('\n', '')
            winner, loser = line.split(' ')
            # print(winner, loser)
            w_name, w_score, l_name, l_score = get_scores(winner, loser)
            team_goals_scored[w_name] = team_goals_scored[w_name] + w_score
            team_goals_scored[l_name] = team_goals_scored[l_name] + l_score

            team_goals_allowed[w_name] = team_goals_allowed[w_name] + l_score
            team_goals_allowed[l_name] = team_goals_allowed[l_name] + w_score

            if w_score == l_score:
                team_win_loss_points[w_name] = team_win_loss_points[w_name] + c.POINTS_FOR_TIE
                team_win_loss_points[l_name] = team_win_loss_points[l_name] + c.POINTS_FOR_TIE
                if is_higher_seed(l_name, w_name):
                    team_win_loss_points[w_name] = team_win_loss_points[w_name] + c.UPSET_TIE
            else:
                team_win_loss_points[w_name] = team_win_loss_points[w_name] + c.POINTS_FOR_WIN
                if is_higher_seed(l_name, w_name):
                    team_win_loss_points[w_name] = team_win_loss_points[w_name] + c.UPSET_WIN

    # print(pdict(team_win_loss_points, '    '))
    # print(pdict(team_goals_scored, '    '))
    # print(pdict(team_goals_allowed, '    '))

#getting player teams
d = './players/'
t = './teams/Group '

with open(t+'A.txt', 'r') as f:
    groupa = [''.join(y for y in x if y != '\n') for x in f]
with open(t+'B.txt', 'r') as f:
    groupb = [''.join(y for y in x if y != '\n') for x in f]
with open(t+'C.txt', 'r') as f:
    groupc = [''.join(y for y in x if y != '\n') for x in f]
with open(t+'D.txt', 'r') as f:
    groupd = [''.join(y for y in x if y != '\n') for x in f]

player_teams = {}
for player in os.listdir(d):
    if len(player) > 3 and player[-3:] == 'txt':
        name = player[:player.index('.txt')]
        with open(d+player, 'r') as teampicks:
            # print('********', name.title(), '********')
            teams = []
            for line in teampicks:
                tmp = ''.join(x for x in line if x != '\n')
                teams.append(tmp)
        player_teams[name] = teams

# print(pdict(player_teams))
#calculating scores for each player given what teams they picked
player_scores = {x: 0 for x in player_teams.keys()}

for player in player_teams:
    for team in player_teams[player]:
        player_scores[player] = player_scores[player] + team_win_loss_points[team]

#what happens in a tie breaker, goals scored - goals allowed decides winner
tie = False
# print(pdict(player_scores))
tie_checker = sorted((player_scores[x], [x]) for x in player_scores)[::-1]
if len(tie_checker) > 1:
    max_score = tie_checker[0][0]
    best_players = [x[1][0] for x in tie_checker if x[0] == max_score]
    if len(best_players) > 1:
        tie = True

tie_breaker = {x: 0 for x in player_teams.keys()}
for player in tie_breaker:
    for team in player_teams[player]:
        tie_breaker[player] = tie_breaker[player] + (team_goals_scored[team] - team_goals_allowed[team])

# print(pdict(tie_breaker))
now = str(dt.now()).split('.')[0].replace(':', ';')
# exit()
os.system('mkdir ./results/"' + now + '"')

errors = check()
#writing to folder
with open('./results/'+now+'/errors.txt', 'w+') as f:
    if errors != "":
        f.write(errors)
with open('./results/'+now+'/goals_scored.txt', 'w+') as f:
    f.write(pdict(team_goals_scored))
with open('./results/'+now+'/goals_allowed.txt', 'w+') as f:
    f.write(pdict(team_goals_allowed))
with open('./results/'+now+'/team_points.txt', 'w+') as f:
    f.write(pdict(team_win_loss_points))
with open('./results/'+now+'/players_scores.txt', 'w+') as f:
    time.sleep(2)
    # print((player_scores))
    a = [(player_scores[k], k) for k in player_scores.keys()]
    b = sorted(a)[::-1]
    # print(b)
    c = {x[1]:x[0] for x in b}
    print(pdict(c))
    f.write(pdict(c))
    if tie:
        f.write('\nTie between ' +  ' and '.join(best_players) + ' (winner is the largest number below, which are the differences between the amount of goals scored and let in by the teams each player picked)\n')
        f.write(pdict(tie_breaker))
# with open('./results/'+now+'/winner.txt', 'w+') as f:
#     f.write(pdict(player_scores))



