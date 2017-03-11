# cohash.py [![Build Status](https://travis-ci.org/theharveyz/cohash.py.svg?branch=master)](https://travis-ci.org/theharveyz/cohash.py)
Consistency hash algorithm implementation in Python

# Install
```
pip install cohash
```

# Usage
```
import cohash
ch = cohash.Hash(nodes = [
    '192.168.01',
    '192.168.02',
    '192.168.03',
    '192.168.04',
], vnum = 1000)
key = 'random-key'
print ch.gen(key)
```

# LICENSE
MIT
