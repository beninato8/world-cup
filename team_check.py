import os
import constants as m

#how many times both list a and b have the same element
def times_in_a_list(a, b):
    c = 0
    for x in a:
        for y in b:
            if x == y:
                c += 1
    return c

#main method
def team_count_is_good():
    #players directory and group affiliation directory
    d = './players/'
    t = './teams/Group '

    #what will be returned at the end of the method. duh
    returnstr = ''

    #creating lists from the teams in each group file
    with open(t+'A.txt', 'r') as f:
        groupa = [''.join(y for y in x if y != '\n') for x in f]
    with open(t+'B.txt', 'r') as f:
        groupb = [''.join(y for y in x if y != '\n') for x in f]
    with open(t+'C.txt', 'r') as f:
        groupc = [''.join(y for y in x if y != '\n') for x in f]
    with open(t+'D.txt', 'r') as f:
        groupd = [''.join(y for y in x if y != '\n') for x in f]

    #creating dict where k = players and v = list of each team they picked
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
    #basically just counting how many times each players teams show up in the individual groups
    for key in playerteams:
        numA = times_in_a_list(playerteams[key], groupa)
        numB = times_in_a_list(playerteams[key], groupb)
        numC = times_in_a_list(playerteams[key], groupc)
        numD = times_in_a_list(playerteams[key], groupd)
        current_player_allgood = True
        # making sure you don't have too many players from each group
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

    #"error" message, but nothing actually happens. more of a warning than an error tbh
    if not allgood:
        returnstr += 'Just letting you know that the people below have too many teams.' + "\n"
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

#debugging and stuff
if __name__ == "__main__":
    team_count_is_good()
