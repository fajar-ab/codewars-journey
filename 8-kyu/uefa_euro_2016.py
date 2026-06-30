# Rank  : 8 kyu
# Title : UEFA EURO 2016
# Link  : https://www.codewars.com/kata/57613fb1033d766171000d60


def uefa_euro_2016(teams, scores):
    team1, team2 = teams
    match scores:
        case [score1, score2] if score1 > score2:
            return "At match {0} - {1}, {0} won!".format(team1, team2)
        case [score1, score2] if score1 < score2:
            return "At match {0} - {1}, {1} won!".format(team1, team2)
        case [score1, score2] if score1 == score2:
            return "At match {0} - {1}, teams played draw.".format(team1, team2)
