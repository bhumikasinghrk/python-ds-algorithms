from queues.moving_average import MovingAverage


def test_moving_average():
    m_avg = MovingAverage(3)
    assert m_avg.next(1) == 1
    assert m_avg.next(2) == 1.5
    assert m_avg.next(3) == 2
    assert m_avg.next(4) == 3
