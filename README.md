# Campus Bike Trips

A small data cleaning and visualization project for CS133. Using provided 144 campus bike-share trips from 2025, it explores how trip distance varies by month and station area, and how cost relates to distance and rider type.

## Charts

- **Monthly distance:** Average trip distance by month.
- **Cost vs. distance:** Trip costs for Casual and Member riders.
- **Station areas:** Average trip distance by starting area.

The charts are saved in `charts/`.

## Run the project

> [!NOTE] 
> The cleaned data and charts are already included in this repository. Run the commands below if you want to reproduce them.

Run these commands from the project root.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/clean.py
python src/time_line_chart.py
python src/scatter_plot.py
python src/dot_chart.py
```
