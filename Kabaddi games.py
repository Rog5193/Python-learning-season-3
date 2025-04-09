def game_checker():
    number_of_players = int(input("How many players want to play?"))

    games_played = list(map(int, input(f"Enter {number_of_players} numbers separated by spaces: ").split()))

    if len(games_played) != number_of_players:
        print(f"You were supposed to enter {number_of_players} numbers, but you entered {len(games_played)}.")

        return
    can_play_3_years = [x for x in games_played if x < 3]
            
    groups = len(can_play_3_years) // 3

    if groups == 0:
        print("Sorry! You can't have any team to play for atleast 1 year. :()") 
    elif groups == 1:   
        print(f"You can have {groups} team that can play Kabbadi at least for 3 years!")
    else:  
        print(f"You can have {groups} teams that can play Kabbadi at least for 3 years!")    

game_checker()