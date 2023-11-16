players = {
    "A1": 25, "A2": 24, "A3": 19, "A4": 18, "A5": 16,
    "B1": 23, "B2": 20, "B3": 18, "B4": 17, "B5": 16,
    "C1": 22, "C2": 14, "C3": 13, "C4": 12, "C5": 11,
    "D1": 10, "D2": 9, "D3": 8, "D4": 7, "D5": 6,
    "E1": 5, "E2": 4, "E3": 3, "E4": 2, "E5": 1,
}

sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
print(sorted_players)

