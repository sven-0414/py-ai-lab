## Tournament data
players = [
    {
        "name": "Erik Karlsson",
        "team": "San Jose Sharks",
        "country": "Sweden",
        "score": 92,
        "matches_played": 70,
        "wins": 35,
        "active": True,
    },
    {
        "name": " Sidney Crosby",
        "team": "Pittsburgh Penguins",
        "country": "canada",
        "score": 105,
        "matches_played": 78,
        "wins": 44,
        "active": True,
    },
    {
        "name": "Connor McDavid  ",
        "team": "Edmonton Oilers",
        "country": "CANADA",
        "score": 130,
        "matches_played": 76,
        "wins": 48,
        "active": True,
    },
    {
        "name": "Leon Draisaitl",
        "team": "edmonton oilers",
        "country": "Germany",
        "score": 112,
        "matches_played": 77,
        "wins": 46,
        "active": True,
    },
    {
        "name": "alex ovechkin",
        "team": "Washington Capitals",
        "country": "Russia",
        "score": 88,
        "matches_played": 74,
        "wins": 40,
        "active": True,
    },
    {
        "name": "Patrik Laine",
        "team": "Montreal Canadiens",
        "country": "Finland",
        "score": 45,
        "matches_played": 52,
        "wins": 20,
        "active": False,
    },
    {
        "name": "  Auston Matthews ",
        "team": "Toronto Maple Leafs",
        "country": "USA",
        "score": 110,
        "matches_played": 75,
        "wins": 46,
        "active": True,
    },
    {
        "name": "David Pastrnak",
        "team": "Boston Bruins",
        "country": "czechia",
        "score": 98,
        "matches_played": 77,
        "wins": 42,
        "active": True,
    },
    {
        "name": "Jaromir Jagr",
        "team": "Kladno",
        "country": "Czechia",
        "score": 12,
        "matches_played": 20,
        "wins": 0,
        "active": False,
    },
    {
        "name": "Henrik Lundqvist",
        "team": "Retired",
        "country": "SWEDEN",
        "score": 0,
        "matches_played": 0,
        "wins": 0,
        "active": False,
    },
    {
        "name": "William Nylander",
        "team": "Toronto Maple Leafs",
        "country": "sweden ",
        "score": 97,
        "matches_played": 76,
        "wins": 41,
        "active": True,
    },
    {
        "name": "Rasmus Dahlin",
        "team": "Buffalo Sabres",
        "country": "Sweden",
        "score": 72,
        "matches_played": 78,
        "wins": 30,
        "active": True,
    },
    {
        "name": "Elias  Pettersson",
        "team": "Vancouver Canucks",
        "country": "Sweden",
        "score": 89,
        "matches_played": 75,
        "wins": 43,
        "active": True,
    },
    {
        "name": "Mikko Rantanen",
        "team": "Colorado Avalanche",
        "country": "FINLAND",
        "score": 104,
        "matches_played": 74,
        "wins": 45,
        "active": True,
    },
    {
        "name": "Aleksander Barkov",
        "team": "Florida Panthers",
        "country": "finland",
        "score": 82,
        "matches_played": 73,
        "wins": 44,
        "active": True,
    },
    {
        "name": "Nathan MacKinnon",
        "team": "Colorado Avalanche",
        "country": "Canada",
        "score": 120,
        "matches_played": 77,
        "wins": 45,
        "active": True,
    },
    {
        "name": "Jack Hughes",
        "team": "New Jersey Devils",
        "country": "usa",
        "score": 78,
        "matches_played": 62,
        "wins": 28,
        "active": True,
    },
    {
        "name": "quinn hughes",
        "team": "Vancouver Canucks",
        "country": "USA",
        "score": 91,
        "matches_played": 76,
        "wins": 43,
        "active": True,
    },
    {
        "name": "Kirill Kaprizov",
        "team": "Minnesota Wild",
        "country": "Russia ",
        "score": 96,
        "matches_played": 74,
        "wins": 39,
        "active": True,
    },
    {
        "name": "Lucas Raymond",
        "team": "Detroit Red Wings",
        "country": "Sweden",
        "score": 68,
        "matches_played": 77,
        "wins": 33,
        "active": True,
    },
    {
        "name": "Matty Beniers",
        "team": "Seattle Kraken",
        "country": "USA",
        "score": 18,
        "matches_played": 8,
        "wins": 8,
        "active": True,
    },
]

# # Cleaning up data

players_cleaned = []

for player in players:
    players_cleaned.append(
        {
            key: value.strip().title() if type(value) == str else value
            for key, value in player.items()
        }
    )


# # Filter the tournament

active_players = [p for p in players_cleaned if p["active"]]
three_wins_mimimum_players = [p for p in players_cleaned if p["wins"] >= 3]
top_score_players = [p for p in players_cleaned if p["score"] >= 100]
swedish_players_names = [p["name"] for p in players_cleaned if p["country"] == "Sweden"]
swedish_top_score_players = [
    p for p in players_cleaned if p["country"] == "Sweden" and p["score"] >= 100
]


# # Tournament statistics


countries = {p["country"] for p in players_cleaned}
teams = {p["team"] for p in players_cleaned}
player_scores = {p["name"]: p["score"] for p in players_cleaned}
player_names_wins = {p["name"]: p["wins"] for p in players_cleaned}
top_score_players_dict = {
    p["name"]: p["score"] for p in players_cleaned if p["score"] >= 100
}

# # Combine tournament data

first_names = ["Anna", "David", "Sara", "Leo", "Mika", "Jonas", "Elin", "Tomas"]
last_names = ["Berg", "Lund", "Holm", "Ek", "Ahl", "Sten", "Vik", "Nord"]
ranking_points = [1200, 950, 1430, 1100, 1050, 1320, 880, 1250, 925]

full_names = [f"{first}, {last}" for first, last in zip(first_names, last_names)]
full_names_and_ranking = [
    (f"{first} {last}", points)
    for first, last, points in zip(first_names, last_names, ranking_points)
]

# Ranking system

players_by_score = sorted(players_cleaned, key=lambda p: p["score"], reverse=True)
players_by_most_wins = sorted(players_cleaned, key=lambda p: p["wins"], reverse=True)
players_by_most_matches_played = sorted(
    players_cleaned, key=lambda p: p["matches_played"], reverse=True
)
players_by_name = sorted(players_cleaned, key=lambda p: p["name"])

# # Ranked tournament report

for index, player in enumerate(players_by_score, start=1):
    print(f"{index}. {player['name']} – {player['score']}")

# # Team analysis
chosen_team = "Edmonton Oilers"
players_from_a_team = [p for p in players_cleaned if p["team"] == chosen_team]
print(players_from_a_team)

player_countries = {p["country"] for p in players_cleaned}
player_teams = {p["team"] for p in players_cleaned}
