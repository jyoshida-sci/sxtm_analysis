import numpy as np


def read_file(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract the data
    list_coordinates = []
    list_list_brightness = [[] for _ in range(4)]
    for i, line in enumerate(lines):
        # Read the header
        if i == 0:
            list_header = line.split('\t')
            continue
        else:
            items = line.split('\t')
            x, y, z = map(float, items[:3])
            list_coordinates.append((x, y))
            for c, val in enumerate(map(float, items[3:7])):
                list_list_brightness[c].append(val)
    # Convert to numpy arrays for easier processing
    array_coordinates = np.array(list_coordinates)
    list_array_brightness = []
    for c in range(4):
        list_brightness = list_list_brightness[c]

        # Create a grid for the coordinates
        x_coords = np.unique(array_coordinates[:, 0])
        y_coords = np.unique(array_coordinates[:, 1])
        brightness_grid = np.zeros((x_coords.size, y_coords.size))

        # Fill the grid with brightness values
        for (x, y), b in zip(list_coordinates, list_brightness):
            x_idx = np.where(x_coords == x)[0][0]
            y_idx = np.where(y_coords == y)[0][0]
            brightness_grid[x_idx, y_idx] = b
        list_array_brightness.append(brightness_grid.T)

    x_y_range = {
        "x_range": (x_coords.min(), x_coords.max()),
        "y_range": (y_coords.min(), y_coords.max()),
        "xmin_xmax_ymin_ymax": [x_coords.min(), x_coords.max(), y_coords.min(), y_coords.max()]
    }
    return list_array_brightness, x_y_range


