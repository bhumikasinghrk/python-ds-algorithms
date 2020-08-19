from strings.string_to_integer import string_to_integer


def test_string_to_integer():
    assert string_to_integer("34") == 34
    assert string_to_integer("   100abc") == 100
    assert string_to_integer("  -12vdsr") == -12
    assert string_to_integer("vdsr12") == 0
    assert string_to_integer("  -12  vdsr") == -12
