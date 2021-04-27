"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from collections import defaultdict

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    with open(neo_csv_path, 'r') as file:
        neo_data = [row for row in csv.DictReader(file)]

    neos_dict = {}
    for i in range(len(neo_data)):
        neos_dict[neo_data[i]['pdes']] = NearEarthObject(
            neo_data[i]['pdes'],
            neo_data[i]['name'],
            neo_data[i]['diameter'],
            neo_data[i]['pha']
        )

    return neos_dict


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    with open(cad_json_path, 'r') as file:
        cads_data = sorted(json.load(file)['data'])

    cads_dict = {}

    for i in range(len(cads_data)):
        des = cads_data[i][0]
        time = cads_data[i][3]
        distance = cads_data[i][5]
        velocity = cads_data[i][7]

        if des not in cads_dict:
            cads_dict[des] = []
            cads_dict[des].append(
                {time: CloseApproach(des, time, distance, velocity)})

        else:
            cads_dict[des].append(
                {time: CloseApproach(des, time, distance, velocity)})

    return cads_dict


# Testing - all works well here

# neos_dict = load_neos()
# cads_dict = load_approaches()

# print('Testing load_neos', neos_dict['433'].name)
# print('Testing if the data is new', neos_dict['433'].approaches)
# print('What should have been there, i.e. approaches for the neo',
#       cads_dict['433'])
