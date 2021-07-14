game_started = int(input("Insira a hora do começo de jogo: "))
game_ended = int(input("insira a hora do fim de jogo: "))

if game_started < 24 or game_started > 0:
    print("Valores incorretos")

elif game_ended < 24 or game_ended > 0:
    print("Valores incorretos")

elif game_ended < game_started:
    
    game_ended_am = game_ended + 24
    result =  game_ended_am - game_started
    print(result)
else:
    result =  game_ended - game_started
    print(result)
