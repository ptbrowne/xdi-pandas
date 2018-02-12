XDI Pandas
========================

This modules lets you easily parse [XDI][1] files generated
by Athena and other software into Pandas dataframes.

```python
from xdi_pandas import parse

df = parse('file.chir')
df2 = parse('file2.lcf')
```

### XDI Fields

Fields are defined and validated in `./xdi-pandas/xdi_types.py` following
[the spec][3].

### Running tests

`nosetest` is used for the tests.

`make test` will run the tests

### Repository structure

Thanks to Kenneth Reitz for is super useful [python module directory structure][2].

[1] : https://github.com/XraySpectroscopy/XAS-Data-Interchange
[2] : https://www.kennethreitz.org/essays/repository-structure-and-python
[3] : https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md
