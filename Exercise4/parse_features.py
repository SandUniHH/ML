#!/usr/bin/python3

import re			# regex

filename = './features.txt'
file = open(filename, 'r')

with file as f:
	l = f.readlines()
	images = [[i for i in range(5)] for j in range(60)]

#print(features)

for line in l:
	# image no, feature no, value
	s = re.search('^\s*\[(\d+),(\d+)\] =\s*(\d+\.?\d*)', line)

	if s:
		images[int(s.group(1))-1][int(s.group(2))-1] = float(s.group(3))

# normalise between values -1 and 1

# get min and max values
minvalues = [255.0] * 5
maxvalues = [0.0] * 5

for image in images:
	for i, value in enumerate(image):
		if value < minvalues[i]:
			minvalues[i] = value
		elif value > maxvalues[i]:
			maxvalues[i] = value

"""
print(maxvalues)
print(minvalues)
"""

# normalise
for image in images:
	for j, value in enumerate(image):
		image[j] = (2 * (value - minvalues[j]) / (maxvalues[j] - minvalues[j])) - 1


parsed = []

for i, image in enumerate(images):

	parsedline = '+1 ' if i < 30 else '-1 '
	for j, value in enumerate(images[i]):
		parsedline += ('{}:{} '.format(j+1, value))

	parsed.append(parsedline)

# shuffle the features so they can be split up in training and test set easier
for i, line in enumerate(parsed):
	if i % 2 == 1: continue

	if i == 30: break

	parsed[i], parsed[i + 30] = parsed[i + 30], parsed[i]

for line in parsed:
	print(line)
