import pandas
import matplotlib.pyplot as plt
import os.path


#TODO: Tidy up code to avoid silently updating global variables like an amateur.


def read_file(selection):
    """Takes user selected file and reads the appropriate file and reads lines to a list"""
    data_set = pandas.read_csv(filepath_or_buffer=selection, header=None)
    global lines
    for num in range(len(data_set)):
        lines.append(data_set[0][num])


def start_coords():
    """Returns first coordinates of route"""
    global x_coords
    global y_coords
    x_coords.append(int(lines[0]))
    y_coords.append(int(lines[1]))


def coords_from_directions(directions):
    global x_coords
    global y_coords
    for num in range(len(directions)):
        if directions[num] == "S":
            x_coords.append(x_coords[-1])
            y_coords.append(y_coords[-1] - 1)
        elif directions[num] == "E":
            x_coords.append(x_coords[-1] + 1)
            y_coords.append(y_coords[-1])
        elif directions[num] == "N":
            x_coords.append(x_coords[-1])
            y_coords.append(y_coords[-1] + 1)
        elif directions[num] == "W":
            x_coords.append(x_coords[-1] - 1)
            y_coords.append(y_coords[-1])


def plot_data(x, y):
    """Opens plotted route in new window Requires equal length lists of x and y coordinates."""
    print("Coords:")
    for _ in range(len(x)):
        print(f"({x[_]} , {y[_]})")
    plt.plot(x, y)
    plt.xticks(x)
    plt.yticks(y)
    plt.grid()
    plt.show()


def run_program(selected_route):
    global plotting_route

    # Create list from .txt file
    if os.path.exists(selected_route):
        read_file(selected_route)
    elif selected_route.lower() == "stop":
        exit()
    else:
        print("File not found, please check spelling and case")
        return

    # find initial coordinates
    start_coords()

    # get directions from data
    directions = [direction for direction in lines[2:]]

    # append coordinates lists from directions list
    coords_from_directions(directions)

    # check route is valid
    for _ in x_coords:
        if _ < 0 or _ > 12:
            print("Error: The route is outside of the grid")
            return
    for _ in y_coords:
        if _ < 0 or _ > 12:
            print("Error: The route is outside of the grid")
            return

    # print coordinates for user
    plot_data(x_coords, y_coords)


plotting_route = True
while plotting_route:
    x_coords = []
    y_coords = []
    lines = []

    # User selects route to plot
    run_program(input("Please name the file to be read including file extension (eg. Route001.txt). "
               "File must be in program directory.\nSpelling, case and file extension must be correct.\n"
               "Or enter STOP to exit:\n"))
