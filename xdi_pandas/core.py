# -*- coding: utf-8 -*-
import os
import pandas as pd
import re
import json

from .xdi_types import xdi_fields

metadata_sep = re.compile(':\s+')
end_of_header = re.compile('^#\s*-*$')
end_of_fields = re.compile('^#\s*/*$')


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
            return validator(v)
        except ValueError as e:
            e.args = ('Could not parse %s as %s' % (v, validator), ) + e.args
            raise e


def parse_metadata(filename):
    metadata = {}
    comments = False
    with open(filename) as f:
        for i, l in enumerate(f.readlines()):
            if re.match(end_of_header, l):
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
                splitted = re.split(metadata_sep, l, maxsplit=2)
                if len(splitted) < 2:
                    raise ValueError('Bad field: "%s" is not in  `Key: Value` form.' % l)
                path, value = splitted
                path = path[2:]
                value = parse_metadata_value(path, value.strip())
                set_dict_path(metadata, path, value)
    return metadata


def parse(filename):
    metadata = parse_metadata(filename)
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
        float_precision='round_trip'
    )
    df.metadata = metadata
    return df
