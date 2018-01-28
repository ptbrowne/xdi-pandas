# -*- coding: utf-8 -*-
import os
import pandas as pd
import re
import json

metadata_sep = re.compile(':\s+')


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

def parse_metadata_value(v):
    try:
        return float(v)
    except ValueError as e:
        pass
    if v == 'None':
        return None
    elif v == 'no':
        return False
    elif v == 'yes':
        return True
    else:
        return v


def parse_metadata(filename):
    metadata = {}
    with open(filename) as f:
        for l in f.readlines():
            if l.startswith('#'):
                if l.startswith('# ///'):
                    break

                splitted = re.split(metadata_sep, l, maxsplit=2)
                if len(splitted) < 2:
                    continue
                path, value = splitted
                path = path[2:]
                value = parse_metadata_value(value.strip())
                set_dict_path(metadata, path, value)
    return metadata


def parse(filename):
    metadata = parse_metadata(filename)
    columns = [
        metadata['Column'][str(k)]
        for k in sorted(map(int, metadata['Column'].keys()))
    ]

    data = pd.read_csv(
        filename,
        comment='#',
        sep='\s+',
        header=None,
        names=columns)
    return data
