"""
You are required to implement all the functions below that read and write data about the internal state of our
animal farm.

Our animal farm can be visualized as a 2D grid of enclosures, each with a number of animals, and indexed by their
row and column number. For example, consider the 4x4 grid below:

[
    [17, 23, 58, 9  ],
    [38, 81, 99, 103],
    [1,  39, 13, 29 ],
    [69, 5,  74, 18 ],
]

We can say that there are 81 animals in the enclosure at position p1 = (1, 1) and 74 animals in the enclosure at
position p2 = (3, 2).
"""

from typing_extensions import Self
import numpy as np

class AnimalFarm(object):

    def __init__(self, farm) -> Self:
        """
        Receives a 2D array `farm` as input, which represents the internal state of our farm. The
        integer at position (i, j) tracks how many animals are currently in the enclosure at that position.

        You may translate this into an internal data structure of your choosing at initialization time, below.

        **IMPORTANT**
        When choosing an internal data structure, do keep in mind that, in general, our expected access pattern
        will be read-heavy. That is, we expect to see far more calls to `count()` than to `update()` and your
        solution should be optimized with this in mind. Our test suite reflects this, and expects `count()` to
        run quickly.

        TODO Implement
        """
        self.farm = np.array(farm)


    def count(self, p1, p2) -> int:
        """
        Calculates how many total animals are in all of the enclosures in the rectangular region defined by p1 = (i1, j1)
        at its top left, and p2 = (i2, j2) at its bottom right, inclusive.

        For example, for the farm defined above, `count((1,1), (2,2))` should return `81 + 99 + 39 + 13 = 232`.

        TODO Implement
        """
        i1, j1 = p1
        i2, j2 = p2

        # Compute the sum of all the animals in the relevant portion of the farm
        row_sums = np.sum(self.farm[i1:i2+1, j1:j2+1], axis=1)
        total = np.sum(row_sums)
        return total

    def update(self, p, v):
        """
        Updates the the number of total animals at position p = (i, j) to be v.

        TODO Implement
        """
        i, j = p
        self.farm[i][j] = v

    def dimension(self):
        """
        Gets the dimension of the farm, as a tuple (M, N).

        TODO Implement
        """
        return self.farm.shape
