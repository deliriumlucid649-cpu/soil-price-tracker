# Utilities for Soil Price Tracker

## Soil Classification Function

def classify_soil(moisture_content, organic_matter_content):
    if moisture_content < 10:
        return 'Sandy Soil'
    elif moisture_content >= 10 and moisture_content <= 30:
        return 'Loamy Soil'
    else:
        return 'Clay Soil'

## Unit Conversion Functions

def convert_pounds_to_kilograms(pounds):
    return pounds * 0.45359237

def convert_inches_to_centimeters(inches):
    return inches * 2.54

## Report Generation with CSV Support
import csv

def generate_report(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Moisture Content', 'Organic Matter', 'Soil Type'])
        for row in data:
            writer.writerow(row)  
        
# Example usage:
if __name__ == '__main__':
    sample_data = [
        (5, 2, classify_soil(5, 2)),
        (15, 3, classify_soil(15, 3)),
        (35, 1, classify_soil(35, 1))
    ]
    generate_report(sample_data, 'soil_report.csv')