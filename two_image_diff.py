import copy
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid1
import fileio

if __name__ == '__main__':

    # Read the file
    filename1 = 'Image_2.txt'
    filename2 = 'Image_3.txt'

    list_array_brightness1, x_y_range1 = fileio.read_file(filename1)
    list_array_brightness2, x_y_range2 = fileio.read_file(filename2)

    brightness1 = list_array_brightness1[2] / list_array_brightness1[0]
    brightness2 = list_array_brightness2[2] / list_array_brightness2[0]

    # shift brightness_grid2 by (delta_x, delta_y)
    for delta_x in range(-2, 3):
        for delta_y in range(-2, 3):
            brightness2_shift = copy.deepcopy(brightness2)
            brightness2_shift = np.roll(brightness2_shift, delta_x, axis=0)
            brightness2_shift = np.roll(brightness2_shift, delta_y, axis=1)

            diff_image = brightness1 - brightness2_shift

            # Plot the image
            fig = plt.figure(figsize=(15, 5))
            ax = fig.add_subplot(1, 3, 1)
            divider = mpl_toolkits.axes_grid1.make_axes_locatable(ax)
            cax = divider.append_axes('right', '5%', pad='3%')
            im = ax.imshow(brightness1, extent=x_y_range1["xmin_xmax_ymin_ymax"], origin='lower')
            fig.colorbar(im, cax=cax)
            ax.set_title('Image_initial')
            ax.set_xlabel('X [${\mu}m$]')
            ax.set_ylabel('Y [${\mu}m$]')
            #
            ax = fig.add_subplot(1, 3, 2)
            divider = mpl_toolkits.axes_grid1.make_axes_locatable(ax)
            cax = divider.append_axes('right', '5%', pad='3%')
            im = ax.imshow(brightness2, extent=x_y_range2["xmin_xmax_ymin_ymax"], origin='lower')
            fig.colorbar(im, cax=cax)
            ax.set_title('Image_final')
            ax.set_xlabel('X [${\mu}m$]')
            ax.set_ylabel('Y [${\mu}m$]')
            #
            ax = fig.add_subplot(1, 3, 3)
            divider = mpl_toolkits.axes_grid1.make_axes_locatable(ax)
            cax = divider.append_axes('right', '5%', pad='3%')
            im = ax.imshow(diff_image, extent=x_y_range1["xmin_xmax_ymin_ymax"], origin='lower')
            fig.colorbar(im, cax=cax)
            ax.set_title('Difference')
            ax.set_xlabel('X [${\mu}m$]')
            ax.set_ylabel('Y [${\mu}m$]')
            #
            plt.tight_layout()
            #plt.show()
            plt.savefig(f'diff_image_x{delta_x:+}_y{delta_y:+}.png')

