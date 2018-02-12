XDI Pandas
========================

This modules lets you easily parse XDI files generated
by Athena and other software into Pandas dataframes.

```python
from xdi_pandas import parse

df = parse('file.chir')
df2 = parse('file2.lcf')
```

Running tests
=============

`nosetest` is used for the tests.

`make test` will run the tests

Repository structure
====================

Thanks to Kenneth Reitz for is super useful [python module
directory structure](https://www.kennethreitz.org/essays/repository-structure-and-python)
