from strings.pangram import pangram


def test_pangram():
    assert pangram('Mr. Jock, TV quiz PhD., bags few lynx.')
    assert pangram('abcdefghijklmnopqrstuvwxyz')
    assert not pangram('test')
    assert not pangram('')
    assert pangram('   \n\t!@#$%^&*()_+[]/\;\',./abcdefghijklmnopqrstuvwxyz')
