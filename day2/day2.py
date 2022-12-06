f = open("day2.txt","r")

points = { 'X': 1, 'Y': 2, 'Z': 3,
					 'A': 1, 'B': 2, 'C': 3}
outcomes ={ 'AX': 3, 'AY': 6, 'AZ': 0,
					  'BX': 0, 'BY': 3, 'BZ': 6,
					  'CX': 6, 'CY': 0, 'CZ': 3,
					  'AA': 3, 'AB': 6, 'AC': 0,
					  'BA': 0, 'BB': 3, 'BC': 6,
					  'CA': 6, 'CB': 0, 'CC': 3}
					  
strategies= { 'AX':'C', 'AY':'A', 'AZ':'B',
              'BX':'A', 'BY':'B', 'BZ':'C',
              'CX':'B', 'CY':'C', 'CZ':'A'}
total_score_1 = 0
total_score_2 = 0
for line in f:
	shape = line.split(" ")[1].strip()
	game_1 = line.split(" ")[0].strip() + line.split(" ")[1].strip()
	desired_game = line.split(" ")[0].strip() + strategies[game_1]
	score_1 = points[shape] + outcomes[game_1]
	score_2 = points[strategies[game_1]] + outcomes[desired_game]
	total_score_1 = total_score_1 + score_1
	total_score_2 = total_score_2 + score_2
	print(f'Part 2:{shape} {game_1} {desired_game} {strategies[game_1]} {outcomes[desired_game]} {score_2} {total_score_2}')
	
print(total_score_2)
	
