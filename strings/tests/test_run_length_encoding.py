from strings.run_length_encoding import run_length_encoding


def test_run_length_encoding():
    assert run_length_encoding('abc') == 'abc'
    assert run_length_encoding('aaabbcddd') == 'a3b2cd3'
    assert run_length_encoding('abbbbc') == 'ab4c'
    assert run_length_encoding('') == ''
