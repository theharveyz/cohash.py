# -*- coding: utf-8 -*-
from binascii import crc32

"""consistent hash: 一致性hash算法,python实现

一致性hash算法的特性:
1. 单调性
2. 均衡性
3. 降低分散性
"""


class Hash(object):
    __VERSION__ = '0.1.3'

    # virtual nodes
    _vnodes = dict()
    _nodes = []
    _vnum = 0

    def __init__(self, nodes=[], vnum=0):
        if not nodes:
            raise TypeError('nodes must be a list object and not empty')
        if not (u"%s" % vnum).isnumeric():
            raise TypeError('nodes must be a number')

        self._nodes = set(nodes)  # convert a set
        nl = len(self._nodes)
        vnum = int(vnum)
        self._vnum = nl if vnum <= nl else vnum

    def gen(self, key):
        self._creat_vnodes()
        return self._find_node(key)

    def _creat_vnodes(self):
        for node in self._nodes:
            for i in xrange(self._vnum):
                self._vnodes[Hash._crc32("%i-%s" % (i, node))] = node

    @staticmethod
    def _crc32(key):
        key = str(key)
        return abs(crc32(key))

    def _find_node(self, key):
        key = Hash._crc32(key)
        position = 0
        #  从小到大排序
        for k in sorted(self._vnodes.keys()):
            position = k
            if key < k:
                return self._vnodes[k]
        return self._vnodes[position]

    @classmethod
    def get_version(cls):
        return cls.__VERSION__
