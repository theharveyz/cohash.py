cohash.py 
==================
.. image:: https://badge.fury.io/py/cohash.svg
    :target: https://badge.fury.io/py/cohash
.. image:: https://travis-ci.org/theharveyz/cohash.py.svg?branch=master
    :target: https://travis-ci.org/theharveyz/cohash.py

Consistency hash algorithm implementation in Python

# Install
```
pip install cohash
```

Usage
------------
.. code-block:: python
import cohash
ch = cohash.Hash(nodes = [
    '192.168.01',
    '192.168.02',
    '192.168.03',
    '192.168.04',
], vnum = 1000)
key = 'random-key'
print ch.gen(key)


LICENSE
------------
MIT
