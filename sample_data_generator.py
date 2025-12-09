"""
Sample Strava data generator for testing the dashboard without real Strava data.
Run this script to generate a sample CSV file.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_sample_data(num_activities=100):
    """Generate sample Strava activities data."""
    
    # Define activity types and gear
    activity_types = ['Run', 'Ride', 'Swim', 'Hike', 'Walk']
    gear_types = ['Running Shoes', 'Road Bike', 'Mountain Bike', 'Swimsuit', 'Hiking Boots', None]
    
    # Generate dates (last 6 months)
    start_date = datetime.now() - timedelta(days=180)
    dates = [start_date + timedelta(days=random.randint(0, 180)) for _ in range(num_activities)]
    dates.sort()
    
    data = {
        'Activity Date': dates,
        'Activity Type': [random.choice(activity_types) for _ in range(num_activities)],
        'Distance (km)': np.random.uniform(2, 50, num_activities),
        'Elevation Gain (m)': np.random.uniform(0, 500, num_activities),
        'Moving Time': [f"{random.randint(15, 180)}:00" for _ in range(num_activities)],
        'Elapsed Time': [f"{random.randint(20, 200)}:00" for _ in range(num_activities)],
        'Avg Heart Rate (bpm)': np.random.uniform(100, 180, num_activities),
        'Max Heart Rate (bpm)': np.random.uniform(150, 200, num_activities),
        'Calories (kcal)': np.random.uniform(100, 1000, num_activities),
        'Gear': [random.choice(gear_types) for _ in range(num_activities)],
    }
    
    df = pd.DataFrame(data)
    
    # Round numeric columns
    df['Distance (km)'] = df['Distance (km)'].round(2)
    df['Elevation Gain (m)'] = df['Elevation Gain (m)'].round(0)
    df['Avg Heart Rate (bpm)'] = df['Avg Heart Rate (bpm)'].round(0)
    df['Max Heart Rate (bpm)'] = df['Max Heart Rate (bpm)'].round(0)
    df['Calories (kcal)'] = df['Calories (kcal)'].round(0)
    
    return df

if __name__ == "__main__":
    # Generate sample data
    df = generate_sample_data(num_activities=100)
    
    # Save to CSV
    output_file = "sample_strava_data.csv"
    df.to_csv(output_file, index=False)
    
    print(f"✅ Sample data generated: {output_file}")
    print(f"📊 Generated {len(df)} activities")
    print(f"\nFirst few rows:")
    print(df.head())
    print(f"\nData summary:")
    print(df.describe())
