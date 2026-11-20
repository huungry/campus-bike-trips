import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/clean/cleaned.csv')   

# Average trip distance grew steadily through the year,
# from 9.4 miles in January to 13.4 miles in December.
monthly = (df.dropna(subset=['distance_miles'])     
             .groupby('month')['distance_miles']
             .mean())

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(monthly.index, monthly.values, color='#1f77b4', linewidth=2,
        marker='o', markersize=6)

# label only the start and end points so the change is easy to read
for m in [monthly.index[0], monthly.index[-1]]:
    ax.annotate(f'{monthly[m]:.1f} mi', (m, monthly[m]),
                textcoords='offset points', xytext=(0, 10),
                ha='center', fontsize=10, fontweight='bold')

ax.set_xticks(range(1, 13))
ax.set_xticklabels(month_names)
ax.set_ylim(0, 15)
ax.set_xlabel('Month (2025)')
ax.set_ylabel('Average trip distance (miles)')
ax.set_title('Average trip distance rose ~4 miles from January to December',
             loc='center', fontsize=11, fontweight='bold')
ax.grid(axis='y', color='#e0e0e0', linewidth=0.8)
ax.set_axisbelow(True)
for side in ['top', 'right']:
    ax.spines[side].set_visible(False)

plt.tight_layout()
plt.savefig('charts/time_line_chart.png', dpi=200)
plt.show()
