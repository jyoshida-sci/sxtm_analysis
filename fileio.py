import numpy as np


def read_file(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract the data
    list_coordinates = []
    list_brightness = []
    for i, line in enumerate(lines):
        # Read the header
        if i == 0:
            list_header = line.split('\t')
            continue
        else:
            items = line.split('\t')
            x, y, z = map(float, items[:3])
            ch0 = float(items[3])
            ch1 = float(items[4])
            ch2 = float(items[5])
            ch3 = float(items[6])
            list_coordinates.append((x, y))
            list_brightness.append(ch2)

    # Convert to numpy arrays for easier processing
    array_coordinates = np.array(list_coordinates)
    array_brightness = np.array(list_brightness)

    # Create a grid for the coordinates
    x_coords = np.unique(array_coordinates[:, 0])
    y_coords = np.unique(array_coordinates[:, 1])
    brightness_grid = np.zeros((x_coords.size, y_coords.size))

    # Fill the grid with brightness values
    for (x, y), b in zip(list_coordinates, list_brightness):
        x_idx = np.where(x_coords == x)[0][0]
        y_idx = np.where(y_coords == y)[0][0]
        brightness_grid[x_idx, y_idx] = b
    
    return brightness_grid


