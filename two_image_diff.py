import copy
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid1
import fileio

if __name__ == '__main__':

    # Read the file
    filename1 = 'Image_2.txt'
    filename2 = 'Image_3.txt'

    brightness_grid1 = fileio.read_file(filename1)
    brightness_grid2 = fileio.read_file(filename2)

    # shift brightness_grid2 by (delta_x, delta_y)
    for delta_x in range(-5, 6):
        for delta_y in range(-5, 6):
            
            brightness_grid2_shift = copy.deepcopy(brightness_grid2)
            brightness_grid2_shift = np.roll(brightness_grid2_shift, delta_x, axis=0)
            brightness_grid2_shift = np.roll(brightness_grid2_shift, delta_y, axis=1)

            diff_image = brightness_grid1 - brightness_grid2_shift

            # Plot the image
            fig = plt.figure(figsize=(15, 5))
            ax = fig.add_subplot(1, 3, 1)
            divider = mpl_toolkits.axes_grid1.make_axes_locatable(ax)
            cax = divider.append_axes('right', '5%', pad='3%')
            im = ax.imshow(brightness_grid1.T, origin='lower')
            fig.colorbar(im, cax=cax)
            ax.set_title('Image_initial')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            #
            ax = fig.add_subplot(1, 3, 2)
            divider = mpl_toolkits.axes_grid1.make_axes_locatable(ax)
            cax = divider.append_axes('right', '5%', pad='3%')
            im = ax.imshow(brightness_grid2.T, origin='lower')
            fig.colorbar(im, cax=cax)
            ax.set_title('Image_final')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            #
            ax = fig.add_subplot(1, 3, 3)
            divider = mpl_toolkits.axes_grid1.make_axes_locatable(ax)
            cax = divider.append_axes('right', '5%', pad='3%')
            im = ax.imshow(diff_image.T, origin='lower')
            fig.colorbar(im, cax=cax)
            ax.set_title('Difference')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')

            plt.tight_layout()
            #plt.show()
            plt.savefig(f'diff_image_x{delta_x:+}_y{delta_y:+}.png')


