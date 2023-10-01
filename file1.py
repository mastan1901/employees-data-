#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import datetime

# Function to calculate the time difference between two timestamps
def calculate_time_difference(start_time, end_time):
    start = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    return (end - start).total_seconds() / 3600  # Convert to hours

# Function to process the employee records
def process_employee_records(file_path):
    df = pd.read_csv(file_path)
    employees_meeting_criteria = []

    for index, row in df.iterrows():
        name = row['Employee Name']
        position = row['Position ID']
        start_time = row['Time']
        end_time = row['Time Out']

        # Calculate the time difference for consecutive days
        start_datetime = datetime.datetime.strptime(str(start_time), "%d-%m-%y %H:%M:%S")
        end_datetime = datetime.datetime.strptime(end_time, "%d-%m-%y %H:%M:%S")
        time_difference = (end_datetime - start_datetime).total_seconds() / 3600

        if time_difference >= 7 * 24:
            meeting_criteria.append(f"{name} ({position}) worked for 7 consecutive days")

        if 1 < time_difference < 10:
            meeting_criteria.append(f"{name} ({position}) has less than 10 hours between shifts")

        if time_difference > 14:
            meeting_criteria.append(f"{name} ({position}) worked for more than 14 hours in a single shift")

    return meeting_criteria

file_path = "data.csv" # Replace with the actual path to your CSV file

results = process_employee_records(file_path)

# Print the results
for result in results:
    print(result)

