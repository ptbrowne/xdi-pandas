# -*- coding: utf-8 -*-
import os
import re
import json

import pandas as pd
import numpy as np

from .xdi_types import xdi_fields

metadata_sep = re.compile(':\s+')
end_of_header = re.compile('^#\s*-+$')
end_of_fields = re.compile('^#\s*/+$')


def set_dict_path(d, path, value):
    cur = d
    splitted = path.split('.')
    l = len(splitted)
    for i, t in enumerate(splitted):
        if i != l - 1:
            cur[t] = cur.get(t, {})
        else:
            cur[t] = value
        cur = cur[t]


def parse_metadata_value(path, v):
    if path.startswith('Column.'):
        return v
    else:
        try:
            validator = xdi_fields.get(path, str)
            if validator == str and v == "":
                raise ValueError()
            return validator(v)
        except ValueError as e:
            if validator == str and v == "":
                raise ValueError("Cannot have empty value for %s" % path)
            e.args = ('Could not parse "%s" as %s' % (v, validator), ) + e.args
            raise e


def parse_metadata(filename):
    metadata = {}
    headers = True # True while parsing headers
    comments = False # True while parsing user comments
    with open(filename) as f:
        for i, l in enumerate(f.readlines()):

            if re.match(end_of_header, l):
                headers = False
                break

            if re.match(end_of_fields, l):
                metadata['Comments'] = metadata.get('Comments', [])
                comments = True
                continue

            if i == 0:
                if 'XDI' not in l:
                    raise ValueError('No XDI version in the first line')
                else:
                    metadata['Version'] = tuple(l.strip().split(' ')[1:])
            elif comments:
                metadata['Comments'].append(l[2:-1])
                continue
            else:
                path, value = parse_namespace_tag(l)
                value = parse_metadata_value(path, value.strip())
                set_dict_path(metadata, path, value)
    if headers:
        raise ValueError('File does not contain end of headers token.')
    return metadata

def check_df(df):
    number_nans = df.isnull().sum().sum()
    if number_nans > 0:
        raise ValueError('Missing data resulting in %s NaN%s' % (number_nans, 's' if number_nans > 1 else ''))


def raise_if_startswith_number(s):
    n = None
    try:
        n = int(s[0])
    except ValueError as e:
        pass
    if n is not None:
        raise ValueError('%s should not start with a number' % s)


def parse_namespace_tag(l):
    splitted = re.split(metadata_sep, l)
    if len(splitted) != 2:
        raise ValueError('Bad field: "%s" is not in  `Key: Value` form.' % l.strip())
    path, value = splitted
    path = path[2:] # Remove "# "
    if ":" in path:
        raise ValueError('Bad field: "%s" should not contain ":"' % path)
    if " " in path:
        raise ValueError('Bad field: "%s" should not contain " ". Namespace should be separated from tag with ".".' % path)

    try:
        namespace, tag = path.split('.')
    except ValueError:
        raise ValueError('Bad field: "%s" should be in the form Namespace.tag' % path)

    raise_if_startswith_number(namespace)
    if namespace != 'Column':
        raise_if_startswith_number(tag)

    return path, value

def parse(filename):
    metadata = parse_metadata(filename)

    if not metadata.get('Column'):
        raise ValueError('No Column labels.')

    columns = [
        metadata['Column'][str(k)]
        for k in sorted(map(int, metadata['Column'].keys()))
    ]

    df = pd.read_csv(
        filename,
        comment='#',
        sep='\s+',
        header=None,
        names=columns,
        float_precision='round_trip',
        error_bad_lines=True,
        warn_bad_lines=True,
        dtype={c:np.float64 for c in columns}
    )

    check_df(df)
    return df
