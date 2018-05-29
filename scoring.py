import constants as c
import os
from datetime import datetime as dt
from team_check import team_count_is_good as check

country_to_code = {'Egypt': 'EG', 'Morocco': 'MA', 'Nigeria': 'NG', 'Senegal': 'SN', 'Tunisia': 'TN', 'Australia': 'AU', 'Iran': 'IR', 'Japan': 'JP', 'South Korea': 'KR', 'Saudi Arabia': 'SA', 'Belgium': 'BE', 'Croatia': 'HR', 'Denmark': 'DK', 'England': 'GB', 'France': 'FR', 'Germany': 'DE', 'Iceland': 'IS', 'Poland': 'PL', 'Portugal': 'PT', 'Russia': 'RU', 'Serbia': 'RS', 'Spain': 'ES', 'Sweden': 'SE', 'Switzerland': 'CH', 'Costa Rica': 'CR', 'Mexico': 'MX', 'Panama': 'PA', 'Argentina': 'AR', 'Brazil': 'BR', 'Columbia': 'CO', 'Peru': 'PE', 'Uruguay': 'UY'}
code_to_country = {v:k for k,v in country_to_code.items()}

def get_scores(w, l):
    w_name = code_to_country[w[:2]]
    w_score = int(w[2:])
    l_name = code_to_country[l[:2]]
    l_score = int(l[2:])
    return w_name, w_score, l_name, l_score
def repeat(s, n):
    return ''.join([s for i in range(n)])

def pdict(d, div='    '):
    m = max([len(x) for x in d])
    return '\n'.join([str(x) + repeat(' ', m - len(str(x))) + str(div) + str(d[x]) for x in d])

# print('\n'.join([country_to_code[x] + '    ' + x for x in country_to_code]))

team_goals_scored = {x: 0 for x in country_to_code.keys()}
team_goals_allowed = {x: 0 for x in country_to_code.keys()}
team_win_loss_points = {x: 0 for x in country_to_code.keys()}
# print(team_goals_scored)

with open('team-scores.txt') as scores:
    for line in scores:
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
            else:
                team_win_loss_points[w_name] = team_win_loss_points[w_name] + c.POINTS_FOR_WIN

    # print(pdict(team_win_loss_points, '    '))
    # print(pdict(team_goals_scored, '    '))
    # print(pdict(team_goals_allowed, '    '))

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

player_scores = {x: 0 for x in player_teams.keys()}

for player in player_teams:
    for team in player_teams[player]:
        player_scores[player] = player_scores[player] + team_win_loss_points[team]

# print(pdict(player_scores))
now = str(dt.now()).split('.')[0]
# exit()
os.system('mkdir ./results/"' + now + '"')

errors = check()

with open('./results/'+now+'/errors.txt', 'w+') as f:
    if errors != "":
        f.write(errors)
with open('./results/'+now+'/goals_scored.txt', 'w+') as f:
    f.write(pdict(team_goals_scored))
with open('./results/'+now+'/goals_allowed.txt', 'w+') as f:
    f.write(pdict(team_goals_allowed))
with open('./results/'+now+'/team_points.txt', 'w+') as f:
    f.write(pdict(team_win_loss_points))
with open('./results/'+now+'/players.txt', 'w+') as f:
    f.write(pdict(player_scores))
# with open('./results/'+now+'/winner.txt', 'w+') as f:
#     f.write(pdict(player_scores))