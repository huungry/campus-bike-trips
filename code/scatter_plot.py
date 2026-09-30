import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned.csv')  

# Both rider types pay the same ~8 cents per mile, but Casual riders
# pay an extra ~$1.25 on every trip, so their line sits $1.25 higher.
pts = df.dropna(subset=['distance_miles', 'cost_dollars'])   

colors = {'Casual': '#d62728', 'Member': '#1f77b4'}
markers = {'Casual': '^', 'Member': 'o'}   # shape as well as color, so it works without color

fig, ax = plt.subplots(figsize=(8, 4.5))
for rider, group in pts.groupby('rider_type'):
    ax.scatter(group['distance_miles'], group['cost_dollars'],
               color=colors[rider], marker=markers[rider], alpha=0.7, s=40, edgecolor='white', linewidth=0.5)
    # direct label at the end of each cloud instead of a legend
    last = group.loc[group['distance_miles'].idxmax()]
    ax.text(last['distance_miles'] + 0.4, last['cost_dollars'], rider,
            color=colors[rider], va='center', fontsize=11, fontweight='bold')

# show the ~$1.25 gap at the same distance
ax.annotate('', xy=(12, 0.08 * 12 + 1.25), xytext=(12, 0.08 * 12),
            arrowprops=dict(arrowstyle='<->', color='#555555'))
ax.text(12.3, 0.08 * 12 + 0.62, '≈ $1.25 extra\nper trip', fontsize=9, color='#555555', va='center')

ax.set_xlim(0, 20)
ax.set_ylim(0, 3)
ax.set_xlabel('Trip distance (miles)')
ax.set_ylabel('Trip cost (dollars)')
ax.yaxis.set_major_formatter('${x:.2f}')
ax.set_title('Same 8¢ per mile, but Casual riders pay ~$1.25 more on every trip',
             loc='left', fontsize=11, fontweight='bold')
ax.grid(color='#e0e0e0', linewidth=0.8)
ax.set_axisbelow(True)
for side in ['top', 'right']:
    ax.spines[side].set_visible(False)

plt.tight_layout()
plt.savefig('charts/problem5_chart.png', dpi=200)
plt.show()