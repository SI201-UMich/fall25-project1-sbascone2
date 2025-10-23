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

def find_best_shipmode_by_segment(data):

    sales_data = defaultdict(lambda: defaultdict(lambda: {"total_sales": 0.0, "count": 0}))

    for row in data:
        segment = row["Segment"]
        ship_mode = row["Ship Mode"]
        try:
            sales = float(row["Sales"])
        except ValueError:
            continue

        sales_data[segment][ship_mode]["total_sales"] += sales
        sales_data[segment][ship_mode]["count"] += 1

    results = []
    for segment, modes in sales_data.items():
        best_mode = None
        best_avg = 0.0
        for mode, vals in modes.items():
            avg_sales = vals["total_sales"] / vals["count"]
            if avg_sales > best_avg:
                best_avg = avg_sales
                best_mode = mode
        results.append({
            "Segment": segment,
            "Best Ship Mode": best_mode,
            "Average Sales": round(best_avg, 2)
        })

    return results

def write_results_to_csv(filename, results, headers):

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(results)
    print(f"Results successfully written to {filename}")

#tests

def test_import_csv_to_dicts():
    data = import_csv_to_dicts("SampleSuperstore.csv")
    assert isinstance(data, list)
    assert isinstance(data[0], dict)
    print("test_import_csv_to_dicts passed")

def test_calculate_avg_profit_by_category_region():
    sample = [
        {"Category": "Furniture", "Region": "West", "Profit": "100"},
        {"Category": "Furniture", "Region": "West", "Profit": "300"},
        {"Category": "Office Supplies", "Region": "East", "Profit": "200"}
    ]
    results = calculate_avg_profit_by_category_region(sample)
    assert any(r["Category"] == "Furniture" and r["Region"] == "West" for r in results)
    print("test_calculate_avg_profit_by_category_region passed")

def test_find_best_shipmode_by_segment():
    sample = [
        {"Segment": "Consumer", "Ship Mode": "First Class", "Sales": "500"},
        {"Segment": "Consumer", "Ship Mode": "Standard Class", "Sales": "300"},
        {"Segment": "Corporate", "Ship Mode": "Second Class", "Sales": "800"}
    ]
    results = find_best_shipmode_by_segment(sample)
    assert any(r["Segment"] == "Consumer" for r in results)
    print("test_find_best_shipmode_by_segment passed")

def main():
    data = import_csv_to_dicts("SampleSuperstore.csv")

    avg_profit_results = calculate_avg_profit_by_category_region(data)
    best_shipmode_results = find_best_shipmode_by_segment(data)

    write_results_to_csv("avg_profit_by_category_region.csv", avg_profit_results,
                         ["Category", "Region", "Average Profit"])
    write_results_to_csv("best_shipmode_by_segment.csv", best_shipmode_results,
                         ["Segment", "Best Ship Mode", "Average Sales"])

    print(" All calculations completed successfully.")

#run