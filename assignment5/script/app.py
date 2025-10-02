import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
import os

base_path = os.path.join(os.path.expanduser("~"), "Documents", "Mcgill", "Fall 2025", "COMP370", "comp370-2025", "assignment5", "data")
file_path = os.path.join(base_path, "cleaned_data.csv")


# === Load and preprocess data ===
df = pd.read_csv(file_path, parse_dates=["Created Date", "Closed Date"])

# Filter out rows without Closed Date
df = df.dropna(subset=["Closed Date"])

# Restrict to 2020 data
df = df[df["Created Date"].dt.year == 2024]

# Compute response time in hours
df["Response Hours"] = (df["Closed Date"] - df["Created Date"]).dt.total_seconds() / 3600

# Extract year-month for grouping
df["YearMonth"] = df["Created Date"].dt.to_period("M").dt.to_timestamp()

# Precompute overall monthly averages (for "ALL 2020")
all_monthly = df.groupby("YearMonth")["Response Hours"].mean().reset_index()


# === Prepare data sources ===
source_all = ColumnDataSource(all_monthly)
source_zip1 = ColumnDataSource(dict(YearMonth=[], Response_Hours=[]))
source_zip2 = ColumnDataSource(dict(YearMonth=[], Response_Hours=[]))


# === Widgets ===
zipcodes = sorted(df["Incident Zip"].dropna().unique().astype(str))
zip1_select = Select(title="Zipcode 1", value=zipcodes[0], options=zipcodes)
zip2_select = Select(title="Zipcode 2", value=zipcodes[1], options=zipcodes)


# === Plot ===
p = figure(
    x_axis_type="datetime",
    title="Monthly Avg Response Time (Hours)",
    width=800,
    height=400
)

p.line(x="YearMonth", y="Response Hours", source=source_all,
       line_width=2, color="black", legend_label="All 2024")

line_zip1 = p.line(x="YearMonth", y="Response_Hours", source=source_zip1,
                   line_width=2, color="blue", legend_label="Zipcode 1")

line_zip2 = p.line(x="YearMonth", y="Response_Hours", source=source_zip2,
                   line_width=2, color="red", legend_label="Zipcode 2")

p.xaxis.axis_label = "Month"
p.yaxis.axis_label = "Response Time (hours)"
p.legend.location = "top_left"


# === Update logic ===
def update_zipdata(attr, old, new):
    # Update Zipcode 1
    zip1 = zip1_select.value
    df_zip1 = df[df["Incident Zip"].astype(str) == zip1]
    zip1_monthly = df_zip1.groupby("YearMonth")["Response Hours"].mean().reset_index()
    source_zip1.data = {
        "YearMonth": zip1_monthly["YearMonth"],
        "Response_Hours": zip1_monthly["Response Hours"]
    }

    # Update Zipcode 2
    zip2 = zip2_select.value
    df_zip2 = df[df["Incident Zip"].astype(str) == zip2]
    zip2_monthly = df_zip2.groupby("YearMonth")["Response Hours"].mean().reset_index()
    source_zip2.data = {
        "YearMonth": zip2_monthly["YearMonth"],
        "Response_Hours": zip2_monthly["Response Hours"]
    }

# Attach callbacks
zip1_select.on_change("value", update_zipdata)
zip2_select.on_change("value", update_zipdata)

# Initialize once
update_zipdata(None, None, None)


# === Layout ===
layout = column(zip1_select, zip2_select, p)
curdoc().add_root(layout)
