import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. SETUP: Define the Scope
num_rows = 10000
start_date = datetime(2025, 1, 1)
machines = ['M-101 (Drill)', 'M-102 (Etch)', 'M-103 (Layer)', 'M-104 (Press)', 'M-105 (Finish)']
shifts = ['Day', 'Night']

# 2. GENERATE DATA
data = []

for i in range(num_rows):
    # Time Logic
    date = start_date + timedelta(days=random.randint(0, 365))
    machine = random.choice(machines)
    shift = random.choice(shifts)
    
    # Manufacturing Logic (The "Hidden" Trends)
    # Trend 1: 'M-102 (Etch)' is older and fails more often in the Night shift.
    # Trend 2: High Temperature (>80) causes massive defect spikes.
    
    temperature = random.normalvariate(65, 10) # Avg temp 65, deviation 10
    voltage = random.normalvariate(220, 5)     # Avg voltage 220
    
    # Base Production
    total_units = random.randint(500, 1000)
    defect_rate_base = 0.02 # 2% default failure
    
    # Applying the "Real World" Problems
    if machine == 'M-102 (Etch)' and shift == 'Night':
        defect_rate_base += 0.05 # Add 5% failure rate
    
    if temperature > 80:
        defect_rate_base += 0.10 # Heat spike causes 10% failure
        
    if voltage < 210:
        defect_rate_base += 0.03 # Low voltage causes 3% failure

    # Calculate Defects
    defect_units = int(total_units * defect_rate_base)
    
    # Randomly introduce "Bad Data" (Nulls) to test your cleaning skills
    if random.random() < 0.01: # 1% chance
        total_units = np.nan
        
    data.append([date, machine, shift, temperature, voltage, total_units, defect_units])

# 3. CREATE DATAFRAME
df = pd.DataFrame(data, columns=['Date', 'Machine_ID', 'Shift', 'Temperature', 'Voltage', 'Total_Units', 'Defect_Units'])

# 4. EXPORT
df.to_csv('manufacturing_yield_data.csv', index=False)
print("Dataset Generated: manufacturing_yield_data.csv")
print("Now go build the dashboard!")