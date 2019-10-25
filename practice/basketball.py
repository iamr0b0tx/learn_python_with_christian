#team 1 score
team_1_score = int(input('Enter Team 1 score: '))

#team 2 score
team_2_score = int(input('Enter team 2 Score: '))

#the team that has the ball
team_with_ball = int(input('Which team has the ball, 1 or 2?: '))

#number of seconds left
time_left = int(input('How many seconds left?: '))

#get the points ahead and the team ahead
if team_1_score > team_2_score:
    points_ahead = team_1_score - team_2_score
    team_ahead = 1
    
else:
    points_ahead = team_2_score - team_1_score
    team_ahead = 2

#decrement by 3
points_ahead -= 3

#add/subtract ball possession advantage
if team_ahead == team_with_ball:
    points_ahead += 0.5

else:
    points_ahead -= 0.5

#square the value
points_ahead *= points_ahead

#final check if lead team is safe
if points_ahead > time_left:
    print('Lead team is safe!')

else:
    print('Lead team is not safe!')
