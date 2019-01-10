#
# Collective Knowledge ()
#
#
#
#
# Developer:
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel)

import os
import sys
import json
import re

import pandas as pd
import numpy as np


##############################################################################
# Initialize module

def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return':0}


##############################################################################
# get raw data for repo-widget

def get_raw_data(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    repo_uoa = 'ck-quantum-hackathon-20190127'

    def get_experimental_results(repo_uoa, tags='qck,hackathon-20190127', module_uoa='experiment'):
        r = ck.access({'action':'search', 'repo_uoa':repo_uoa, 'module_uoa':module_uoa, 'tags':tags})
        if r['return']>0:
            print('Error: %s' % r['error'])
            exit(1)
        experiments = r['lst']

        dfs = []
        for experiment in experiments:
            data_uoa = experiment['data_uoa']
            r = ck.access({'action':'list_points', 'repo_uoa':repo_uoa, 'module_uoa':module_uoa, 'data_uoa':data_uoa})
            if r['return']>0:
                print('Error: %s' % r['error'])
                exit(1)

            # For each point.
            for point in r['points']:
                point_file_path = os.path.join(r['path'], 'ckp-%s.0001.json' % point)
                with open(point_file_path) as point_file:
                    point_data_raw = json.load(point_file)
                choices = point_data_raw['choices']
                characteristics_list = point_data_raw['characteristics_list']
                num_repetitions = len(characteristics_list)
                data = [
                    {
                        # statistical repetition
                        'repetition_id': repetition_id,
                        # runtime characteristics
                        'problem': characteristics['run'].get('problem',''),
                        'circuit': characteristics['run'].get('circuit',''),
                        'cost': np.float64(characteristics['run'].get('cost',1e6)),
                        'source_code': characteristics['run'].get('source_code',''),
                        'test_accuracy': np.float64(characteristics['run'].get('test_accuracy',0.0)),
                        'success?': characteristics['run'].get('run_success','N/A'),
                    }
                    for (repetition_id, characteristics) in zip(range(num_repetitions), characteristics_list)
                    if len(characteristics['run']) > 0
                ]

                index = [
                    'problem'
                ]

                # Construct a DataFrame.
                df = pd.DataFrame(data)
                df = df.set_index(index)
                # Append to the list of similarly constructed DataFrames.
                dfs.append(df)
        if dfs:
            # Concatenate all thus constructed DataFrames (i.e. stack on top of each other).
            result = pd.concat(dfs)
            result.sort_index(ascending=True, inplace=True)
        else:
            # Construct a dummy DataFrame the success status of which can be safely checked.
            result = pd.DataFrame(columns=['success?'])
        return result


    # prepare table
    df = get_experimental_results(repo_uoa=repo_uoa)

    table = []

    def to_value(i):
        if type(i) is np.ndarray:
            return i.tolist()

        if isinstance(i, np.int64):
            return int(i)

        return i

    props = [
        '_problem',
        'success?',
    ]

    for record in df.to_dict(orient='records'):
        row = {}
        for prop in props:
            row[prop] = to_value(record.get(prop, ''))

#        row['##data_uid'] = "{}:{}".format(record['_point'], record['_repetition_id'])
#
#        row['_minimizer_src'] = {
#            'title': record.get('_minimizer_method','Show'),
#            'cmd': record['_minimizer_src']
#           }

        table.append(row)

    return {'return':0, 'table':table}


##############################################################################
# get raw config for repo widget

def get_raw_config(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

#    data_config = cfg['data_config']
    data_config['return'] = 0

    return data_config
