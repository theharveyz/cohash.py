import pytest
from chash import CHash

def test_crc32():
    foo = 'foo'
    i = 1
    assert CHash._crc32(foo) == abs(-1938594527)
    assert CHash._crc32(i) == CHash._crc32('%s' % i) == abs(-2082672713)

def test_exceptions():
    try:
        ch = CHash([])
    except TypeError, e:
        assert e.message.find('list')
    finally:
        assert False

    try:
        ch = CHash(['a'], 'a')
    except TypeError, e:
        assert e.message.find('number')
    finally:
        assert False

def test_gen():
    nodes = ['a', 'b', 'c', 1]
    vnum = 100
    ch = CHash(nodes=nodes, vnum=vnum)
    key = 'foo'
    assert ch.gen(key) in nodes
