import pytest
from cohash import Hash

def test_crc32():
    foo = 'foo'
    i = 1
    assert Hash._crc32(foo) == abs(-1938594527)
    assert Hash._crc32(i) == Hash._crc32('%s' % i) == abs(-2082672713)

def test_exceptions():
    try:
        ch = Hash([])
    except TypeError, e:
        assert e.message.find('list')
    else:
        assert False

    try:
        ch = Hash(['a'], 'a')
    except TypeError, e:
        assert e.message.find('number')
    else:
        assert False

def test_gen():
    nodes = ['a', 'b', 'c', 1]
    vnum = 100
    ch = Hash(nodes=nodes, vnum=vnum)
    key = 'foo'
    assert ch.gen(key) in nodes
