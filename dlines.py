import sys
import matplotlib.pyplot as plt

DISTANCE = 0.5

def draw_lines(ax, coordinates):

    if len(coordinates) < 3: 
        return

    plot_coordinates(ax, coordinates, "yellow")
    is_horizontal_line = does_it_repeat_y(coordinates, 0)

    red_prev_x, red_prev_y, blue_prev_x, blue_prev_y = get_starting_points(coordinates, 0, is_horizontal_line)

    red_coordinates = [(red_prev_x, red_prev_y)]
    blue_coordinates = [(blue_prev_x, blue_prev_y)]

    print(" prev red: ", red_prev_x, red_prev_y, " prev blue: ", blue_prev_x, blue_prev_y)
    for i in range(1, len(coordinates) - 1):
        red_next_x, red_next_y, blue_next_x, blue_next_y = get_next_points(red_prev_x, red_prev_y, blue_prev_x, blue_prev_y, coordinates, i, is_horizontal_line)
        
        red_coordinates.append((red_next_x, red_next_y))
        blue_coordinates.append((blue_next_x, blue_next_y))
        
        is_horizontal_line = not is_horizontal_line
        red_prev_x, red_prev_y = red_next_x, red_next_y
        blue_prev_x, blue_prev_y = blue_next_x, blue_next_y
        #print(" prev red: ", red_prev_x, red_prev_y, " prev blue: ", blue_prev_x, blue_prev_y)

    
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

    red_x, red_y, blue_x, blue_y = get_ending_points(coordinates, len(coordinates) - 1, is_horizontal_line)
    #print(" out red: ", red_x, red_y, " blue: ", blue_x, blue_y)
    #print(" out prev red: ", red_prev_x, red_prev_y, " prev blue: ", blue_prev_x, blue_prev_y)
    red_coordinates.append((red_x, red_y))
    blue_coordinates.append((blue_x, blue_y))
    
    plot_coordinates(ax, red_coordinates, "red")
    plot_coordinates(ax, blue_coordinates, "blue")

def get_starting_points(coordinates, p, is_horizontal_line):
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

def get_ending_points(coordinates, p, is_horizontal_line):
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


def get_next_points(red_prev_x, red_prev_y, blue_prev_x, blue_prev_y, coordinates, p, is_horizontal_line):
    x1, y1 = coordinates[p] # B
    x2, y2 = coordinates[p + 1] # C
    red_next_x, red_next_y = red_prev_x, red_prev_y
    blue_next_x, blue_next_y = blue_prev_x, blue_prev_y
    if is_horizontal_line:
        if y1 < y2:
            red_next_x = x1 - DISTANCE
            blue_next_x = x1 + DISTANCE
        else: 
            red_next_x = x1 + DISTANCE
            blue_next_x = x1 - DISTANCE
    else: 
        if x1 < x2:
            red_next_y = y1 + DISTANCE
            blue_next_y = y1 - DISTANCE
        else: 
            red_next_y = y1 - DISTANCE
            blue_next_y = y1 + DISTANCE
    return (red_next_x, red_next_y, blue_next_x, blue_next_y)

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


fig, ax = plt.subplots()

# actual work
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
ax.set_title('Double Lines')

# Display legend
ax.legend()

# Show the plot
plt.show()


