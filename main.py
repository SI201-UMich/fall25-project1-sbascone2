"""
Project 1: Data Analysis - SI 201
Name: Sophie Bascone
Student ID: sbascone
Email: sbascone@umich.edu
Collaborators: Used ChatGPT for instruction on structure and debugging assistance
Dataset: Sample Superstore
"""

import csv
from collections import defaultdict


def import_csv_to_dicts(filename):
    """
    Reads a CSV file and returns a list of dictionaries.
    Each dictionary represents a row in the dataset.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data
