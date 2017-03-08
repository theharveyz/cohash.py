# -*- coding: utf-8 -*-

from binascii import crc32

"""consistent hash: 一致性hash算法,python实现

一致性hash算法的特性:
1. 单调性
2. 均衡性
3. 降低分散性
"""

class CHash(object):

	# virtual nodes
	_vnodes = dict()

	_nodes = []

	_vnum = 0

	def __init__(self, nodes = [], vnum = 0):
		if not nodes:
			raise ValueError('nodes must be a list object')
		if not (u"%s" % vnum).isnumeric():
			raise ValueError('nodes must be a number')

		self._nodes = set(nodes) # convert a set
		nl = len(self._nodes)
		vnum = int(vnum)
		self._vnum = nl if vnum <= nl else vnum

	def gen(self, key):
		self._creat_vnodes()
		return self._find_node(key)

	def _creat_vnodes(self):
		for node in self._nodes:
			for i in xrange(self._vnum):
				self._vnodes[CHash._crc32("%i-%s" % (i, node))] = node

	@staticmethod
	def _crc32(key):
		return abs(crc32(key))

	def _find_node(self, key):
		key = CHash._crc32(key)
		position = 0
		# 从大到小排序
		for k in sorted(self._vnodes.keys()):
			position = k
			if key < k:
				return self._vnodes[k]
		return self._vnodes[position]
