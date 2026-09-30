import pandas as pd 

df = pd.read_csv('data/CS133-Assignment-04-dataset.csv')

# convert text in numeric columns
for col in ['start_hour', 'distance_miles', 'duration_minutes', 'cost_dollars']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# remove any rows with 0.0 duration_minutes but with non-zero distance_miles
df = df[(df['distance_miles'] > 0.0) & (df['duration_minutes'] != 0.0)]

# remove any trailing whitespace
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

# fix capitalization
df['station_area'] = df['station_area'].str.title()
df['rider_type'] = df['rider_type'].str.title()
df['weather'] = df['weather'].str.title()

# Sort by trip_date
df['trip_date'] = pd.to_datetime(df['trip_date'])
df = df.sort_values(by='trip_date')

# Add a column for month (numeric 1 - 12)
df['month'] = df['trip_date'].dt.month

# Add a column for speed
df['speed_mph'] = df['distance_miles'] / df['duration_minutes'] * 60

# save to csv file
df.to_csv('data/cleaned.csv', index=False)