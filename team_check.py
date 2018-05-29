import os
import constants as m

def times_in_a_list(a, b):
    c = 0
    for x in a:
        for y in b:
            if x == y:
                c += 1
    return c

def team_count_is_good():
    d = './players/'
    t = './teams/Group '
    returnstr = ''
    with open(t+'A.txt', 'r') as f:
        groupa = [''.join(y for y in x if y != '\n') for x in f]
    with open(t+'B.txt', 'r') as f:
        groupb = [''.join(y for y in x if y != '\n') for x in f]
    with open(t+'C.txt', 'r') as f:
        groupc = [''.join(y for y in x if y != '\n') for x in f]
    with open(t+'D.txt', 'r') as f:
        groupd = [''.join(y for y in x if y != '\n') for x in f]

    playerteams = {}
    for player in os.listdir(d):
        if len(player) > 3 and player[-3:] == 'txt':
            name = player[:player.index('.txt')]
            with open(d+player, 'r') as teampicks:
                # print('********', name.title(), '********')
                teams = []
                for line in teampicks:
                    tmp = ''.join(x for x in line if x != '\n')
                    teams.append(tmp)
            playerteams[name] = teams

    # print(playerteams)
    numA = 0
    numB = 0
    numC = 0
    numD = 0
    allgood = True
    error_people = set([''])
    for key in playerteams:
        numA = times_in_a_list(playerteams[key], groupa)
        numB = times_in_a_list(playerteams[key], groupb)
        numC = times_in_a_list(playerteams[key], groupc)
        numD = times_in_a_list(playerteams[key], groupd)
        current_player_allgood = True
        if numA > m.A:
            returnstr += 'Too many teams from Group A for %s' % key.title() + "\n"
            current_player_allgood = False
        if numB > m.B:
            returnstr += 'Too many teams from Group B for %s' % key.title() + "\n"
            current_player_allgood = False
        if numC > m.C:
            returnstr += 'Too many teams from Group C for %s' % key.title() + "\n"
            current_player_allgood = False
        if numD > m.D:
            returnstr += 'Too many teams from Group D for %s' % key.title() + "\n"
            current_player_allgood = False
        if not current_player_allgood:
            error_people.add(key.title())
            allgood = False

    if not allgood:
        returnstr += 'The people below have too many teams. Please fix it and try again.' + "\n"
        returnstr += ''.join('*' for i in range(len(max(error_people)))) + "\n"
        returnstr += '\n'.join([x for x in error_people])[1:] + "\n"
        returnstr += ''.join('*' for i in range(len(max(error_people)))) + "\n"
        # return False
        return returnstr
    else:
        returnstr += 'All teams look OK!' + "\n"
        # return returnstr
        return ""
    # return True
if __name__ == "__main__":
    team_count_is_good()
