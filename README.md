# XDI Pandas

This modules lets you easily parse <a
href="https://github.com/XraySpectroscopy/XAS-Data-Interchange">XDI</a> files
generated into Pandas dataframes. It supports several Athena extension fields.


```python
from xdi_pandas import parse

df = parse('file.chir')
df2 = parse('file2.lcf')
```
### XDI Fields

Fields are defined and validated in [./xdi-pandas/xdi_types.py] following <a
href="https://github.com/XraySpectroscopy/XAS-Data-
Interchange/blob/master/specification/dictionary.md">the spec</a>.

Supported fields :

```bash
$ python -c 'from xdi_pandas.xdi_types import xdi_fields; print("\n".join(xdi_fields.keys()))'
Beamline.collimation
Beamline.focusing
Beamline.harmonic_rejection
Beamline.name
Detector.i0
Detector.it
Detector.if
Detector.ir
Element.edge
Element.symbol
Element.reference
Element.ref_edge
Mono.d_spacing
Mono.name
Facility.current
Facility.energy
Athena.bkg_kweight
Athena.clamps
Athena.dk
Athena.dr
Athena.e0
Athena.edge_step
Athena.eshift
Athena.fixed_step
Athena.importance
Athena.k_range
Athena.kweight
Athena.normalization_range
Athena.phase_correction
Athena.plot_multiplier
Athena.post_edge_polynomial
Athena.pre_edge_line
Athena.pre_edge_range
Athena.r_range
Athena.rbkg
Athena.spline_range_energy
Athena.spline_range_k
Athena.standard
Athena.window
Athena.y_offset
Scan.start_time
Scan.end_time
Scan.edge_energy
Sample.name
Sample.id
Sample.stoichiometry
Sample.prep
Sample.experimenters
Sample.temperature

```
### Tests

`nosetest` is used for the tests.

`make test` will run the tests
### Repository structure

Thanks to Kenneth Reitz for is super useful <a
href="https://www.kennethreitz.org/essays/repository-structure-and-
python">python module directory structure</a>.
