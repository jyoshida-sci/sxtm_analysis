import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Read the file
    filename = 'Image_3.txt'
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract the data
    list_coordinates = []
    list_brightness = []
    list_x = []
    list_y = []
    list_z = []
    list_val0 = []
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
            # list_x.append(x)
            # list_y.append(y)
            # list_z.append(z)

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

    # Plot the image
    plt.imshow(brightness_grid.T, extent=[x_coords.min(), x_coords.max(), y_coords.min(), y_coords.max()], origin='lower')
    plt.colorbar(label='Brightness')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Brightness Distribution')
    plt.show()





"""
X	Y	Z	ch0	ch1	ch2	ch3	ch4	ch5	ch6	2024/07/17	12:24:47
-30.000	-29.000	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-28.800	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-28.600	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-28.400	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-28.200	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-28.000	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-27.800	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-27.600	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-27.400	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-27.200	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-27.000	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
-30.000	-26.800	0.000	6.758630E-1	2.174609E+0	2.039843E-1	-4.964189E-3
"""