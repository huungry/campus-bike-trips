import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned.csv')   

dist = (df.dropna(subset=['distance_miles'])
          .groupby('station_area')['distance_miles']
          .mean()
          .sort_values())

highlight = ['Engineering', 'Library']
colors = ['#1f77b4' if s in highlight else '#b0b0b0' for s in dist.index]

fig, ax = plt.subplots(figsize=(7, 3.5))
ax.hlines(dist.index, 0, dist.values, color=colors, linewidth=2)
ax.scatter(dist.values, dist.index, color=colors, s=90, zorder=3)
for y, x in enumerate(dist.values):
    ax.text(x + 0.2, y, f'{x:.1f} mi', va='center', fontsize=10)

ax.set_xlim(0, 14)
ax.set_xlabel('Average trip distance (miles)')
ax.set_ylabel('Station area')
ax.set_title('Engineering and Library riders go ~3 miles farther',
             loc='left', fontsize=11, fontweight='bold')
for side in ['top', 'right']:
    ax.spines[side].set_visible(False)

plt.tight_layout()
plt.savefig('charts/problem3_chart.png', dpi=200)
plt.show()