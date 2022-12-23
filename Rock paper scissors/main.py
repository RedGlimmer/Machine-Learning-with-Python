from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player, player_v2, player_rps

print("Player:")
play(player, quincy, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)

print("\nPlayer_v2:")
play(player_v2, quincy, 1000)
play(player_v2, abbey, 1000)
play(player_v2, kris, 1000)
play(player_v2, mrugesh, 1000)

print("\nplayer_v2 vs player:")
play(player_v2, player, 1000)

print("\nplayer_v2 vs R-P-S pattern player")
play(player_v2, player_rps, 1000)

# Uncomment line below to play interactively against a bot:
# play(human, player_v2, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(player_v2, random_player, 1000)