import sys
import matplotlib.pyplot as plt

# How far away from initial points we want to draw the double lines
DISTANCE = 0.5

def draw_lines(ax, coordinates):

    if len(coordinates) < 3: 
        return

    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    is_horizontal_line = (y1 == y2)

    red_x, red_y, blue_x, blue_y = get_extremities(coordinates, 0, 1, is_horizontal_line, True)
    red_coordinates = [(red_x, red_y)]
    blue_coordinates = [(blue_x, blue_y)]

    for i in range(1, len(coordinates) - 1):
        red_x, red_y, blue_x, blue_y = get_next_points(red_x, red_y, blue_x, blue_y, coordinates, i, is_horizontal_line)        
        red_coordinates.append((red_x, red_y))
        blue_coordinates.append((blue_x, blue_y))
        is_horizontal_line = not is_horizontal_line

    red_x, red_y, blue_x, blue_y = get_extremities(coordinates, len(coordinates) - 1, len(coordinates) - 2, is_horizontal_line, False)
    red_coordinates.append((red_x, red_y))
    blue_coordinates.append((blue_x, blue_y))
    
    plot_coordinates(ax, coordinates, "yellow")
    plot_coordinates(ax, red_coordinates, "red")
    plot_coordinates(ax, blue_coordinates, "blue")


def get_extremities(coordinates, a, b, is_horizontal_line, is_start):
    a_x, a_y = coordinates[a]
    b_x, b_y = coordinates[b]

    if is_horizontal_line:
        if (a_x > b_x) == is_start:
            return a_x, a_y - DISTANCE, a_x, a_y + DISTANCE
        else:
            return a_x, a_y + DISTANCE, a_x, a_y - DISTANCE
    else:
        if (a_y > b_y) == is_start: 
            return a_x + DISTANCE, a_y, a_x - DISTANCE, a_y
        else:
            return a_x - DISTANCE, a_y, a_x + DISTANCE, a_y


def get_next_points(red_prev_x, red_prev_y, blue_prev_x, blue_prev_y, coordinates, p, is_horizontal_line):
    x1, y1 = coordinates[p]
    x2, y2 = coordinates[p + 1]
    if is_horizontal_line:
        if y1 < y2:
            return x1 - DISTANCE, red_prev_y, x1 + DISTANCE, blue_prev_y
        else: 
            return x1 + DISTANCE, red_prev_y, x1 - DISTANCE, blue_prev_y
    else: 
        if x1 < x2:
            return red_prev_x, y1 + DISTANCE, blue_prev_x, y1 - DISTANCE
        else: 
            return red_prev_x, y1 - DISTANCE, blue_prev_x, y1 + DISTANCE


def does_it_repeat_y(coordinates, p):
    x1, y1 = coordinates[p]
    x2, y2 = coordinates[p + 1]
    if x1 == x2:
        return False
    elif y1 == y2:
        return True

def plot_coordinates(ax, coordinates, line_color):
    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]
        ax.plot([x1, x2], [y1, y2], color=line_color)

# Main
if len(sys.argv) > 1:
    coordinates = [(float(sys.argv[i]), float(sys.argv[i + 1])) for i in range(1, len(sys.argv), 2)]
else:
    n = int(input("Enter the number of coordinates: "))
    coordinates = []
    for i in range(n):
        input_str = input(f"Enter x{i+1} y{i+1} (separated by space): ")
        x, y = map(float, input_str.split())
        coordinates.append((x, y))

fig, ax = plt.subplots()

# Actual work
draw_lines(ax, coordinates)

# Plotting stuff
min_x = min(x for x, y in coordinates) - 3
max_x = max(x for x, y in coordinates) + 3
min_y = min(y for x, y in coordinates) - 3
max_y = max(y for x, y in coordinates) + 3
ax.set_xlim(min_x, max_x)
ax.set_ylim(min_y, max_y)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Double Lines')
plt.show()


