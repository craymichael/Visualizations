# =====================================================================
# xor.py - 3D Bitwise XOR function visualization.
# Copyright (C) 2018  Zach Carmichael
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# =====================================================================
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import FormatStrFormatter
import numpy as np

DEFAULT_N = 32


def xor_integers_in_bounds(n_neg, n_pos):
    """ All points in 2-dimensional range x = [n_neg, n_pos-1]
        and y = [n_neg, n_pos-1] are selected from specified
        range. Bitwise xor is applied pointwise and the results
        returned.

    Args:
        n_neg: The negative bound
        n_pos: The positive bound
    Returns:
        x: The x coords in range [n_neg, n_pos]
        y: The y coords in range [n_neg, n_pos]
        pointwise bitwise xor
    """
    points = np.mgrid[n_neg:n_pos, n_neg:n_pos]
    x = points[0].flatten()
    y = points[1].flatten()
    return x, y, np.bitwise_xor(x, y)


def visualize_xor(n_neg, n_pos):
    # Get xor result
    x, y, xor = xor_integers_in_bounds(n_neg, n_pos)
    # 3D plot
    f = plt.figure()
    ax = f.add_subplot(111, projection='3d')
    ax.scatter(x, y, xor, s=8)
    # Format z-axis limits as integers
    ax.zaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.set_title('Bitwise XOR Applied Pointwise to $x \in [{}, {}]$ '
                 'and $y \in [{}, {}]$.'.format(n_neg, n_pos - 1,
                                                n_neg, n_pos - 1))
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    for i, (elev, angle) in enumerate(zip([25, 25, 90 + 25],
                                          [90, 0, -90])):
        ax.view_init(elev=elev, azim=angle)
        plt.savefig('xor_3D_plot_axis_' + ('xyz'[i]) + '.png', dpi=300)
    ax.view_init(elev=25, azim=90)
    plt.show()


if __name__ == '__main__':
    import argparse


    def main(args):
        # Bounds
        n_neg = -args.n
        n_pos = args.n
        # Plot
        visualize_xor(n_neg, n_pos)


    parser = argparse.ArgumentParser(description='Visualize bitwise xor operation.')
    parser.add_argument('--n', type=int, help='Plot given bounds [-n, n-1] (default is '
                                              '[{}, {}]).'.format(-DEFAULT_N, DEFAULT_N - 1),
                        default=DEFAULT_N)
    args = parser.parse_args()
    main(args)
