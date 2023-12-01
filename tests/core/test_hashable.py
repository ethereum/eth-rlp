import pytest
from rlp.sedes import (
    big_endian_int,
)

from eth_rlp import (
    HashableRLP,
)


class TwoIntRLP(HashableRLP):
    fields = (
        ("pos1", big_endian_int),
        ("pos2", big_endian_int),
    )


@pytest.mark.parametrize(
    "unserialized, expected_hash_hex",
    (([0, 1], "0x698b0c299d3182774bd859102bea2f205f0a1b3674c8d1d7aee6b17122a2f73a"),),
)
def test_hash(unserialized, expected_hash_hex):
    rlp_obj = TwoIntRLP(*unserialized)
    assert rlp_obj.hash().hex() == expected_hash_hex


@pytest.mark.parametrize(
    "unserialized, expected_hash_hex",
    (
        (
            {"pos1": 0, "pos2": 1},
            "0x698b0c299d3182774bd859102bea2f205f0a1b3674c8d1d7aee6b17122a2f73a",
        ),
    ),
)
def test_create_with_dict(unserialized, expected_hash_hex):
    assert TwoIntRLP.from_dict(unserialized).hash().hex() == expected_hash_hex


@pytest.mark.parametrize(
    "serialized, expected_hash_hex, expected_fields",
    (
        (
            b"\xc2\x80\x01",
            "0x698b0c299d3182774bd859102bea2f205f0a1b3674c8d1d7aee6b17122a2f73a",
            {"pos1": 0, "pos2": 1},
        ),
    ),
)
def test_from_bytes(serialized, expected_hash_hex, expected_fields):
    rlp_obj = TwoIntRLP.from_bytes(serialized)
    assert rlp_obj.hash().hex() == expected_hash_hex
    for name, val in expected_fields.items():
        assert getattr(rlp_obj, name) == val


@pytest.mark.parametrize(
    "unserialized, expected_fields",
    (
        (
            {"pos2": 1, "pos1": 0},
            [0, 1],
        ),
    ),
)
def test_iteration(unserialized, expected_fields):
    rlp_obj = TwoIntRLP(**unserialized)
    for actual, expected in zip(rlp_obj, expected_fields):
        assert actual == expected
    assert list(rlp_obj) == expected_fields


@pytest.mark.parametrize(
    "unserialized, expected_dict",
    (
        (
            {"pos2": 1, "pos1": 0},
            {"pos2": 1, "pos1": 0},
        ),
    ),
)
def test_to_dict(unserialized, expected_dict):
    rlp_obj = TwoIntRLP(**unserialized)
    assert rlp_obj.as_dict() == expected_dict
