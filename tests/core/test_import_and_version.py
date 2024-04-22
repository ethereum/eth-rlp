def test_import_and_version():
    import eth_rlp

    assert isinstance(eth_rlp.__version__, str)
