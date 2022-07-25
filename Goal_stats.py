
import pandas as pd


# Get Matches from Men's Euro 2020
matches = pd.read_csv("Matches.csv")

teamnametype = 'home_team.home_team_name'
scoretype1 = 'home_score'
scoretype2 = 'away_score'

matchid = []
team_name = []
goals_for = []
goals_against = []
goal_diff = []
outcomes = []

for i in range(0,51):

    matchid1 = matches.loc[i, 'match_id']

    team_name1 = matches.loc[i, teamnametype]

    # Find scores
    goals_for1 = matches.loc[i, scoretype1]
    goals_against1 = matches.loc[i, scoretype2]

    # Calculate goal differential
    goal_diff1 = goals_for1 - goals_against1

    # Determine win, loss, or tie
    outcome = ""
    if goals_for1 > goals_against1:
        outcome = "win"
    elif goals_for1 < goals_against1:
        outcome = "loss"
    else:
        outcome = "tie"

    matchid.append(matchid1)
    team_name.append(team_name1)
    goals_against.append(goals_against1)
    goals_for.append(goals_for1)
    goal_diff.append(goal_diff1)
    outcomes.append(outcome)



# away teams
teamnametype = 'away_team.away_team_name'
scoretype2 = 'home_score'
scoretype1 = 'away_score'


for i in range(0,51):

    matchid1 = matches.loc[i, 'match_id']

    team_name1 = matches.loc[i, teamnametype]

    # Find scores
    goals_for1 = matches.loc[i, scoretype1]
    goals_against1 = matches.loc[i, scoretype2]

    # Calculate goal differential
    goal_diff1 = goals_for1 - goals_against1

    # Determine win, loss, or tie
    outcome = ""
    if goals_for1 > goals_against1:
        outcome = "win"
    elif goals_for1 < goals_against1:
        outcome = "loss"
    else:
        outcome = "tie"

    matchid.append(matchid1)
    team_name.append(team_name1)
    goals_against.append(goals_against1)
    goals_for.append(goals_for1)
    goal_diff.append(goal_diff1)
    outcomes.append(outcome)

# Create DF and spreadsheet
df = pd.DataFrame({'match_id' : matchid, 'team_name' : team_name, 'goals_for' : goals_for, 'goals_against' : goals_against, 'goal_diff' : goal_diff, 'outcome' : outcomes})
df.to_csv('bymatch_stats.csv', index=False)