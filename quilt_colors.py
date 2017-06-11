import random
from itertools import product
from typing import Iterable, Sequence


class Block:
    """A quilt block."""

    def __init__(self, color_pallet: Iterable[str]):
        """:param color_pallet: The possible colors for this `Block`."""
        self.color = None
        self.color_pallet = set(color_pallet)

        # the `Quilt` must set the neighbors attribute after instantiation
        # because not all of the block's neighbors exist when it is instantiated.
        self.neighbors = None

    @property
    def adjacent_colors(self) -> set:
        """The colors of adjacent blocks."""
        return {n.color for n in self.neighbors} - {None}

    def choose_color(self):
        """Choose a color for this block that none of it's neighbors have."""
        self.color = random.choice(list(self.color_pallet - self.adjacent_colors))


class Quilt:
    """A quilt that can color itself with a random pattern."""
    _adjacency = [p for p in product((-1, 0, 1), (-1, 0, 1)) if p != (0, 0)]

    def __init__(self, width: int, height: int, color_pallet: Sequence[str]):
        """
        :param width: the width of the quilt in `Blocks`.
        :param height: the height of the quilt in `Blocks`.
        :param color_pallet: A sequence of **single** character strings.
            If the strings are longer than one character they will be truncated
            when printing the `Quilt`.
        """
        if len(color_pallet) < 5:
            # technically 4 colors is enough to choose colors that don't touch.
            # However it requires a very regular pattern that doesn't look random.
            raise ValueError('Not enough colors to choose from. '
                             'Try adding colors to your pallet.')

        self.grid = [[Block(color_pallet) for _ in range(width)] for _ in range(height)]
        for y, row in enumerate(self.grid):
            for x, block in enumerate(row):
                block.neighbors = tuple(self._iter_neighbors(x, y))

    def _iter_neighbors(self, x, y):
        for i, j in self._adjacency:
            try:
                yield self.grid[y + j][x + i]
            except IndexError:  # We tried to get a block that doesn't exits.
                pass

    def choose_colors(self):
        """Find a new color pattern for the `Quilt`."""
        for _ in range(10_000):
            try:
                for row in self.grid:
                    for block in row:
                        block.choose_color()
                return
            except IndexError:
                # We ran into a dead end trying to choose unique colors
                # quilts are not that big, just start over.
                continue

    def __str__(self):
        # lay out the colors in a grid so you can see them
        return '\n\n'.join(' '.join(b.color[:] for b in row) for row in self.grid)

    def __repr__(self):
        return (
            f'{self.__class__.__name__}('
            f'width={len(self.grid[0])}, '
            f'height={len(self.grid)}, '
            f'color_pallet={list(self.grid[0][0].color_pallet)}'
            f')'
        )
