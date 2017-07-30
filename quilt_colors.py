from itertools import chain
from random import shuffle, seed
from typing import TypeVar, Tuple, Union, Any, Set, Iterable, Iterator

seed()
Color = TypeVar('Color')


def assign_color(color: Color,
                 quilt: Tuple[Tuple[Union[Color, None], ...], ...],
                 x: int,
                 y: int) -> Tuple[Tuple[Union[Color, None], ...], ...]:
    """
    Create a new quilt with block (`x`, `y`) has the color `color`.

    :param color: The color to give the specified block.
    :param quilt: The quilt to be colored.
    :param x: The block's x position.
    :param y: The block's y position.
    :return: A new quilt with the newly colored block.
    """
    old_row = quilt[y]
    new_row = old_row[:x] + (color,) + old_row[x+1:]
    return quilt[:y] + (new_row,) + quilt[y+1:]


def neighbors(quilt: Tuple[Tuple[Any, ...], ...], x: int, y: int) -> Set[Any]:
    """
    Get the color of all neighbors.

    .. note::

        The color of block (`x`, `y`) is included in the colors returned.

    :param quilt: The quilt containing (x, y)'s neighbors.
    :param x: The block's x position.
    :param y: The block's y position.
    :return: The set of all neighboring colors.
    """
    left, up = max(x-1, 0), max(y-1, 0)  # negative indexes are not allowed
    return set(chain(*(row[left:x+2] for row in quilt[up:y+2])))


def next_empty(quilt: Tuple[Tuple[Any, ...], ...]) -> Union[Tuple[int, int], None]:
    """
    Get the position of the next empty block in the `quilt`.

    Empty blocks are populated with None.

    :param quilt: The quilt to be searched for empty blocks.
    :return: The position of the next empty block i.e. (x, y)
             or None if there are no empty blocks.
    """
    for y, row in enumerate(quilt):
        try:
            return row.index(None), y
        except ValueError:
            continue
    return None  # there were no empty blocks


def random_order(values: Iterable[Any]) -> Iterator[Any]:
    """
    Get an iterator that yields items from `values` in a random order.

    :param values: A collection of values.
    :return: A randomly ordered iterator.
    """
    list_ = list(values)
    shuffle(list_)
    return iter(list_)


def color_quilt(quilt: Tuple[Tuple[Union[Color, None], ...], ...],
                colors: Set[Color]) -> Union[Tuple[Tuple[Color, ...], ...], None]:
    """
    Randomly assign colors to a `quilt` without letting any colors touch.

    :param quilt: The empty quilt to be colored.
    :param colors: The set of colors to choose from.
    :return: A randomly colored quilt or None if there is no solution.
    """
    block = next_empty(quilt)
    if block is None:
        return quilt  # No more empty blocks. => The quilt is fully colored!
    valid_colors = colors - neighbors(quilt, *block)
    for color in random_order(valid_colors):
        child_quilt = assign_color(color, quilt, *block)
        finished_quilt = color_quilt(child_quilt, colors)
        if finished_quilt is not None:
            return finished_quilt  # We found a solution!
    return None  # There is no solution in this branch.


def print_quilt(quilt: Tuple[Tuple[Any, ...], ...]) -> None:
    """
    Print a quilt with fixed width columns.

    :param quilt: The quilt to be printed.
    """
    width = max(len(str(c)) for c in chain(*quilt))
    spec = f'{{:^{width}}}'
    print()
    for row in quilt:
        formatted = (spec.format(c) for c in row)
        print(' '.join(formatted), end='\n\n')


def new_quilt(width: int, height: int) -> Tuple[Tuple[None, ...], ...]:
    """
    Create a new empty quilt.

    :param width: The quilt width in blocks.
    :param height: The quilt height in blocks.
    :return: An empty quilt.
    """
    return tuple(tuple(None for _ in range(width)) for _ in range(height))


if __name__ == '__main__':
    quilt = new_quilt(10, 15)
    answer = color_quilt(quilt, {'red', 'green', 'blue', 'yellow', 'mauve'})
    if answer is None:
        print(None)
    else:
        print_quilt(answer)
