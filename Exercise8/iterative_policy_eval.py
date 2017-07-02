#!/usr/bin/python3

import numpy as np

def initialize(SIZE_GRID, ACTIONS):

	act_prob = 1 / len(ACTIONS)

	world = create_world(SIZE_GRID)

	# set possible actions in the world
	steps = []

	for i in range(0, SIZE_GRID):
		steps.append([]) # new x axis line
		for j in range(0, SIZE_GRID):
			move = dict() # possible move depending on current field

			# possible steps on the borders
			if i == 0:
				move['up'] = [i,j] # don't actually move
			else:
				move['up'] = [i - 1, j]

			if i == SIZE_GRID - 1: # bottom
				move['down'] = [i, j]
			else:
				move['down'] = [i + 1, j]

			if j == 0: # left border
				move['left'] = [i, j]
			else:
				move['left'] = [i, j - 1]

			if j == SIZE_GRID - 1: # right border
				move['right'] = [i, j]
			else:
				move['right'] = [i, j + 1]

			steps[i].append(move)

	# create the states in the world except for the terminal states.
	# thus, the terminal state values will never be changed from 0.0
	states = []
	for i in range(0, SIZE_GRID):
		for j in range(0, SIZE_GRID):
			if (i == 0 and j == 0) or \
				(i == SIZE_GRID -1 and j == SIZE_GRID -1):
				continue
			else:
				states.append([i,j])

	return world, states, steps, act_prob

def create_world(SIZE_GRID):

	return np.zeros((SIZE_GRID, SIZE_GRID)) # square world

def evaluate(world, states, steps, act_prob, ACTIONS, REWARD, SIGMA):

	delta_small_enough = False
	k = 0

	while not delta_small_enough: # no do - while in Python

		new_world = create_world(SIZE_GRID)
		k += 1

		for i, j in states:
			for action in ACTIONS:
				do_step = steps[i][j][action] # do_step is v

				# Bellmann equation
				new_world[i,j] += act_prob * \
								  (REWARD + world[do_step[0], do_step[1]])

		# check whether Delta is smaller than sigma
			Delta = np.sum(np.abs(world - new_world))
			if Delta < SIGMA:
				delta_small_enough = True

		world = new_world

	return k, new_world

####
SIZE_GRID = 4 # one axis
REWARD = -1
ACTIONS = ['up', 'left', 'down', 'right']

# start with 0.2, lower it until the low amount of desired iterations is reached
#sigma = 0.2
sigma = 1e-10

world, states, steps, act_prob = initialize(SIZE_GRID, ACTIONS)
k, new_world = evaluate(world, states, steps, act_prob, ACTIONS, REWARD, sigma)
print('iterations: {}, sigma: {}'.format(k, sigma))

'''
while k > 10:

	sigma = sigma * 1.01
	k, new_world = evaluate(world, states, steps, act_prob, ACTIONS, REWARD,
							  sigma)
	print('iterations: {}, sigma: {}'.format(k, sigma))
'''

print(new_world)

# iterations for sigma == 0.2: 79
# iterations: sigma < 1: 49

'''
iterations: 79, sigma: 0.2
[[  0.         -13.81911086 -19.73195486 -21.70004164]
 [-13.81911086 -17.76386809 -19.73374791 -19.73195486]
 [-19.73195486 -19.73374791 -17.76386809 -13.81911086]
 [-21.70004164 -19.73195486 -13.81911086   0.        ]]

iterations: 470, sigma: 1e-10
[[  0. -14. -20. -22.]
 [-14. -18. -20. -20.]
 [-20. -20. -18. -14.]
 [-22. -20. -14.   0.]]


'''