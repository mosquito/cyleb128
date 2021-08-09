LEB128
======

Cython implementation LEB128 varint serialization format.

Installation
------------

```shell
pip install cyleb128
```

Example
-------

```python
from leb128 import LEB128S, LEB128U

# Signed integer
print(LEB128S.encode(-123))
print(LEB128S.decode(LEB128S.encode(-321)))

# Unsigned integer
print(LEB128U.encode(123))
print(LEB128U.decode(LEB128S.encode(123)))
```
