import pytest
from leb128 import LEB128S, LEB128U


ENCODE_CASES = [
    (LEB128U.encode, 624485, b'\xe5\x8e&'),
    (LEB128S.encode, -123456, b'\xc0\xbbx'),
]


@pytest.mark.parametrize("func, value, expected", ENCODE_CASES)
def test_encode(func, value, expected):
    assert func(value) == expected


DECODE_CASES = [
    (LEB128U.decode, b"\xe5\x8e\x26", 624485),
    (LEB128S.decode, b"\xc0\xbb\x78", -123456),
]


@pytest.mark.parametrize("func, value, expected", DECODE_CASES)
def test_decode(func, value, expected):
    assert func(value) == expected


TWO_WAY_CASES = [
    (LEB128U, 624485),
    (LEB128S, -123456),
]


@pytest.mark.parametrize("klass, value", TWO_WAY_CASES)
def test_two_way(klass, value):
    assert value == klass.decode(klass.encode(value))
    assert klass.encode(value) == klass.encode(
        klass.decode(klass.encode(value))
    )
