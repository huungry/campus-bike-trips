import pandas as pd

df = pd.read_csv('../data/cleaned.csv') # I used 2 dots because it needed when on Jupyter

# rain doesn't change how far people ride, but it slows them down,
# so rainy trips take longer to complete. 
table = (
    df.groupby('weather')
      .agg(trips=('trip_id', 'count'),
           avg_distance=('distance_miles', 'mean'),    
           avg_duration=('duration_minutes', 'mean'),
           avg_speed=('speed_mph', 'mean'))
      .sort_values('avg_speed', ascending=False)       # fastest -> slowest, Rain ends up last
)

# difference from clear-weather trips makes the message explicit
table['extra_minutes_vs_clear'] = table['avg_duration'] - table.loc['Clear', 'avg_duration']

table = table.rename(columns={
    'trips': 'Trips',
    'avg_distance': 'Avg distance (mi)',
    'avg_duration': 'Avg duration (min)',
    'avg_speed': 'Avg speed (mph)',
    'extra_minutes_vs_clear': 'Extra minutes vs. Clear',
})
table.index.name = 'Weather'

styled = (
    table.style
    .format({'Avg distance (mi)': '{:.1f}',
             'Avg duration (min)': '{:.1f}',
             'Avg speed (mph)': '{:.1f}',
             'Extra minutes vs. Clear': '{:+.1f}'})
    .set_caption('Rain slows campus riders by about 4 mph, adding ~11 minutes per trip')
    .apply(lambda row: ['font-weight: bold; background-color: #dbe9f6'
                        if row.name == 'Rain' else '' for _ in row], axis=1)
)
styled  # displays in Jupyter