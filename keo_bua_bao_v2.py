import random
import string

keo = 'kéo'
bua = 'búa'
bao = 'bao'
options = [keo, bua, bao]


def competition(player_name1, player_name2) -> string:
    """Return name of player who is lost"""
    score1 = 0
    score2 = 0

    print("** Trận đấu của: \"{}\" vs \"{}\" ! **".format(player_name1, player_name2))
    while abs(score1 - score2) != 2:
        player_choice1 = random.choice(options)
        player_choice2 = random.choice(options)

        print("Người chơi \"{}\" ra: {}.".format(player_name1, player_choice1))
        print("Người chơi \"{}\" ra: {}.".format(player_name2, player_choice2))

        if player_choice1 == player_choice2:
            score1 += 0.5
            score2 += 0.5
        elif player_choice1 == keo:
            if player_choice2 == bua:
                score2 += 1
            else:
                score1 += 1
        elif player_choice1 == bua:
            if player_choice2 == bao:
                score2 += 1
            else:
                score1 += 1
        else:
            if player_choice2 == keo:
                score2 += 1
            else:
                score1 += 1

        print(
            "\"{}\" được {} điểm - \"{}\" được {} điểm.".format(player_name1, score1, player_name2, score2))
        print("--------")

    if score1 > score2:
        print("Người chơi \"{}\" đã chiến thắng người chơi \"{}\".\n".format(player_name1, player_name2))
        return player_name2
    else:
        print("==Người chơi \"{}\" đã chiến thắng người chơi \"{}\".==\n".format(player_name2, player_name1))
        return player_name1


if __name__ == '__main__':
    numbers_of_players = random.choice(range(8, 21))

    print("Có {} tham gia trò chơi này.\n".format(numbers_of_players))

    rest_players = []
    for i in range(numbers_of_players):
        rest_players.append("Player {}".format(i + 1))

    while len(rest_players) > 1:
        index1 = random.choice(range(0, len(rest_players)))
        index2 = random.choice(range(0, len(rest_players)))
        while index1 == index2:
            index2 = random.choice(range(0, len(rest_players)))

        result = competition(rest_players[index1], rest_players[index2])
        rest_players.remove(result)

    print("Người chiến thắng trò chơi là \"{}\".\n".format(rest_players[0]))
