import sys
import matplotlib.pyplot as plt

DISTANCE = 0.5
# vertical down, vertical up
# python3 dlines.py 2 9 2 6 8 6 8 9 5 9 5 13
# vertical down, vertical up
# python3 dlines.py 5 13 5 9 8 9 8 6 2 6 2 9
# vertical up, vertical down
# python3 dlines.py 10 10 10 13 7 13 7 10 4 10 4 7 7 7 7 4 13 4 13 1 16 1 16 12 13 12 13 9 11 9 11 2
# horizontal left, horizontal left
# python3 dlines.py 10 13 7 13 7 10 4 10 4 7 7 7 7 4 13 4 13 1 16 1 16 12 13 12 13 9 11 9 11 2 10 2 
# horizontal right, horizontal right
# python3 dlines.py 9 11 10 11 10 13 7 13 7 10 4 10 4 7 7 7 7 4 13 4 13 1 16 1 16 12 13 12 13 9 11 9 11 6 18 6

def draw_lines(ax, coordinates):

    if len(coordinates) < 3: 
        return

    plot_coordinates(ax, coordinates, "yellow")
    is_horizontal_line = does_it_repeat_y(coordinates, 0)

    red_prev_x, red_prev_y, blue_prev_x, blue_prev_y = get_extreme_points(coordinates, 0, is_horizontal_line)

    red_coordinates = [(red_prev_x, red_prev_y)]
    blue_coordinates = [(blue_prev_x, blue_prev_y)]

    print(" prev red: ", red_prev_x, red_prev_y, " prev blue: ", blue_prev_x, blue_prev_y)
    for i in range(1, len(coordinates) - 1):
        red_next_x, red_next_y = get_next_red_point(red_prev_x, red_prev_y, coordinates, i, is_horizontal_line)
        blue_next_x, blue_next_y = get_next_blue_point(blue_prev_x, blue_prev_y, coordinates, i, is_horizontal_line)
        
        red_coordinates.append((red_next_x, red_next_y))
        blue_coordinates.append((blue_next_x, blue_next_y))
        
        is_horizontal_line = not is_horizontal_line
        red_prev_x, red_prev_y = red_next_x, red_next_y
        blue_prev_x, blue_prev_y = blue_next_x, blue_next_y
        print(" prev red: ", red_prev_x, red_prev_y, " prev blue: ", blue_prev_x, blue_prev_y)

    
    red_x, red_y = blue_x, blue_y = coordinates[len(coordinates) - 1]

    # last point is different
    if is_horizontal_line:
        # red_x is done
        red_y = red_y - DISTANCE
        blue_y = blue_y + DISTANCE
    else:
        # red_y is done
        red_x = red_x + DISTANCE
        blue_x = blue_x - DISTANCE

    red_x, red_y, blue_x, blue_y = get_extreme_points2(coordinates, len(coordinates) - 1, is_horizontal_line)
    print(" out red: ", red_x, red_y, " blue: ", blue_x, blue_y)
    print(" out prev red: ", red_prev_x, red_prev_y, " prev blue: ", blue_prev_x, blue_prev_y)
    red_coordinates.append((red_x, red_y))
    blue_coordinates.append((blue_x, blue_y))
    
    plot_coordinates(ax, red_coordinates, "red")
    plot_coordinates(ax, blue_coordinates, "blue")
    #ax.plot([red_prev_x, red_prev_y], [last_x, last_y], color="red")
    #ax.plot([blue_prev_x, blue_prev_y], [last_x, last_y], color="blue") 


def get_extreme_points(coordinates, p, is_horizontal_line):
    red_x, red_y = blue_x, blue_y = a_x, a_y = coordinates[p]
    b_x, b_y = coordinates[p + 1]
    if is_horizontal_line:
        if a_x > b_x: # left  
            red_y = a_y - DISTANCE
            blue_y = a_y + DISTANCE
        else: # right
            red_y = a_y + DISTANCE
            blue_y = a_y - DISTANCE
    else:
        if a_y > b_y: # vertival down 
            red_x = a_x + DISTANCE
            blue_x = a_x - DISTANCE
        else: # vertical up
            red_x = a_x - DISTANCE
            blue_x = a_x + DISTANCE
    return red_x, red_y, blue_x, blue_y



def get_extreme_points2(coordinates, p, is_horizontal_line):
    red_x, red_y = blue_x, blue_y = a_x, a_y = coordinates[p]
    b_x, b_y = coordinates[p - 1]
    if is_horizontal_line:
        if a_x > b_x: # left  
            red_y = a_y + DISTANCE
            blue_y = a_y - DISTANCE
        else: # right
            red_y = a_y - DISTANCE
            blue_y = a_y + DISTANCE
    else:
        if a_y > b_y: # vertival down 
            red_x = a_x - DISTANCE
            blue_x = a_x + DISTANCE
        else: # vertical up
            red_x = a_x + DISTANCE
            blue_x = a_x - DISTANCE
    return red_x, red_y, blue_x, blue_y


def get_next_red_point(prev_x, prev_y, coordinates, p, is_horizontal_line):
    x1, y1 = coordinates[p] # B
    x2, y2 = coordinates[p + 1] # C
    next_x, next_y = prev_x, prev_y
    if is_horizontal_line:
        if y1 < y2:
            next_x = x1 - DISTANCE
        else: 
            next_x = x1 + DISTANCE
    else: 
        if x1 < x2:
            next_y = y1 + DISTANCE
        else: 
            next_y = y1 - DISTANCE
    return (next_x, next_y)


def get_next_blue_point(prev_x, prev_y, coordinates, p, is_horizontal_line):
    x1, y1 = coordinates[p] # B
    x2, y2 = coordinates[p + 1] # C
    next_x, next_y = prev_x, prev_y
    if is_horizontal_line:
        if y1 < y2:
            next_x = x1 + DISTANCE
        else: 
            next_x = x1 - DISTANCE
    else: 
        if x1 < x2:
            next_y = y1 - DISTANCE
        else: 
            next_y = y1 + DISTANCE
    return (next_x, next_y)

def does_it_repeat_y(coordinates, p):
    x1, y1 = coordinates[p]
    x2, y2 = coordinates[p + 1]
    if x1 == x2:
        return False
    elif y1 == y2:
        return True

def plot_coordinates(ax, coordinates, line_color):
    # plot regular line
    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]
        ax.plot([x1, x2], [y1, y2], color=line_color)

# Check if command line arguments are provided
if len(sys.argv) > 1:
    # Extract coordinates from command line arguments
    coordinates = [(float(sys.argv[i]), float(sys.argv[i + 1])) for i in range(1, len(sys.argv), 2)]
else:
    # Read coordinates from user input
    n = int(input("Enter the number of coordinates: "))
    coordinates = []
    for i in range(n):
        input_str = input(f"Enter x{i+1} y{i+1} (separated by space): ")
        x, y = map(float, input_str.split())
        coordinates.append((x, y))

# Create a figure and axis
fig, ax = plt.subplots()

# Call the function to draw lines connecting all points
draw_lines(ax, coordinates)

# Set axis limits
min_x = min(x for x, y in coordinates) - 3
max_x = max(x for x, y in coordinates) + 3
min_y = min(y for x, y in coordinates) - 3
max_y = max(y for x, y in coordinates) + 3
ax.set_xlim(min_x, max_x)
ax.set_ylim(min_y, max_y)

# Set axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set plot title
ax.set_title('Lines Connecting All Points')

# Display legend
ax.legend()

# Show the plot
plt.show()


