import subprocess
import random

python_script = 'dlines.py'

MIN = 0
MAX = 50
N = 15 # number of points in each test
M = 3 # number of auto created test cases

def generate_coordinates(N):
    coordinates = []

    changelings = random.sample(range(MIN, MAX), N + 1)
    # print(changelings)

    x = changelings[0]
    y = changelings[1]
    coordinates.append((x, y))
    repeat_x = True
    for i in range(N - 1): 
        changeling = changelings[i + 2]
        if repeat_x:
            coordinates.append((x, changeling))
            y = changeling
        else: 
            coordinates.append((changeling, y))
            x = changeling
        repeat_x = not repeat_x
    return coordinates

# manually created tests
argument_lists = [
    ['5', '13', '5', '9', '8', '9', '8', '6', '2', '6', '2', '9'],
    ['2', '9', '2', '6', '8', '6', '8', '9', '5', '9', '5', '13', '2', '13'],
    ['10', '10', '10', '13', '7', '13', '7', '10', '4', '10', '4', '7', '7', '7', '7', '4', '13', '4', '13', '1', '16', '1', '16', '12', '13', '12', '13', '9', '11', '9', '11', '2'],
    ['10', '13', '7', '13', '7', '10', '4', '10', '4', '7', '7', '7', '7', '4', '13', '4', '13', '1', '16', '1', '16', '12', '13', '12', '13', '9', '11', '9', '11', '2', '10', '2'],
    ['9', '11', '10', '11', '10', '13', '7', '13', '7', '10', '4', '10', '4', '7', '7', '7', '7', '4', '13', '4', '13', '1', '16', '1', '16', '12', '13', '12', '13', '9', '11', '9', '11', '6', '18', '6'],
]

# uncomment to skip manually created tests
# argument_lists = []
for _ in range(M):
    coordinates = generate_coordinates(N)
    string_array = [str(coord) for point in coordinates for coord in point]
    formmated = ' '.join([f"\n({x}, {y})" for x, y in coordinates])
    print(formmated)
    argument_lists.append(string_array)

for args in argument_lists:
    command = ['python3', python_script] + args
    subprocess.run(command)

