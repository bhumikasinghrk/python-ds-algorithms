from strings.crop_string import crop_string


def test_crop_string():
    assert crop_string('test', 9) == 'test'
    assert crop_string('test', 3) == ''
    assert crop_string('test', 4) == 'test'
    assert crop_string('test test', 6) == 'test'
    assert crop_string('', 4) == ''
    assert crop_string('test test', 9) == 'test test'

