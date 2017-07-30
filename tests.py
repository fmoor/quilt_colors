from quilt_colors import next_empty, assign_color, neighbors


def test_next_empty_first():
    quilt = ((None, 1, 1),
             (None, 1, 1),
             (None, 1, 1),)
    assert next_empty(quilt) == (0, 0)


def test_next_empty_last():
    quilt = ((1, 1, 1),
             (1, 1, 1),
             (1, 1, None),)
    assert next_empty(quilt) == (2, 2)


def test_next_empty_side():
    quilt = ((1, 1, 1),
             (1, 1, None),
             (1, 1, 1),)
    assert next_empty(quilt) == (2, 1)


def test_next_empty_middle():
    quilt = ((1, 1, 1),
             (1, None, 1),
             (1, 1, 1),)
    assert next_empty(quilt) == (1, 1)


def test_assign_color_top_left():
    quilt = ((0, 0, 0, 0),
             (0, 0, 0, 0),
             (0, 0, 0, 0),
             (0, 0, 0, 0),)
    assert assign_color(1, quilt, 0, 0) == ((1, 0, 0, 0),
                                            (0, 0, 0, 0),
                                            (0, 0, 0, 0),
                                            (0, 0, 0, 0),)


def test_assign_color_bottom_right():
    quilt = ((0, 0, 0, 0),
             (0, 0, 0, 0),
             (0, 0, 0, 0),
             (0, 0, 0, 0),)
    assert assign_color(1, quilt, 3, 3) == ((0, 0, 0, 0),
                                            (0, 0, 0, 0),
                                            (0, 0, 0, 0),
                                            (0, 0, 0, 1),)


def test_neighbors():
    quilt = ((1, 2, 3, 0),
             (8, 9, 4, 0),
             (7, 6, 5, 0),
             (0, 0, 0, 0),)
    assert neighbors(quilt, 1, 1) == {1, 2, 3, 4, 5, 6, 7, 8, 9}


def test_neighbors_top_left():
    quilt = ((1, 2, 3, 0),
             (8, 9, 4, 0),
             (7, 6, 5, 0),
             (0, 0, 0, 0),)
    assert neighbors(quilt, 0, 0) == {1, 2, 8, 9}


def test_neighbors_bottom_right():
    quilt = ((0, 0, 0, 0),
             (0, 0, 0, 0),
             (0, 0, 5, 2),
             (0, 0, 6, 1),)
    assert neighbors(quilt, 3, 3) == {1, 2, 5, 6}