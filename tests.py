from pytest import fixture

from quilt_colors import Block


@fixture
def color_pallet():
    return 'rgbyc'


@fixture
def neighbor(color_pallet):
    return Block(color_pallet)


@fixture
def block(color_pallet, neighbor):
    block = Block(color_pallet)
    block.neighbors = [neighbor]
    return block


def test_block_finds_adjacent_colors(block, neighbor):
    neighbor.color = 'r'
    assert block.adjacent_colors == {'r'}


def test_block_adjacent_colors_doesnt_contain_none(block):
    assert block.adjacent_colors == set()


def test_block_chooses_color_from_color_pallet(block, color_pallet):
    assert block.color is None
    block.choose_color()
    assert block.color in color_pallet
