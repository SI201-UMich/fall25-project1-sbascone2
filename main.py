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
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def calculate_avg_profit_by_category_region(data):

    profit_data = defaultdict(lambda: {"total_profit": 0.0, "count": 0})

    for row in data:
        category = row["Category"]
        region = row["Region"]
        try:
            profit = float(row["Profit"])
        except ValueError:
            continue

        key = (category, region)
        profit_data[key]["total_profit"] += profit
        profit_data[key]["count"] += 1

    results = []
    for (category, region), vals in profit_data.items():
        avg_profit = vals["total_profit"] / vals["count"]
        results.append({
            "Category": category,
            "Region": region,
            "Average Profit": round(avg_profit, 2)
        })

    return results
