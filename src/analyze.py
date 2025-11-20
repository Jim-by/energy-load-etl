import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting up chart styles
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["font.size"] = 12

# Directory paths
PROCESSED_DIR = os.path.join("data", "processed")
PLOTS_DIR = os.path.join("plots")
os.makedirs(PLOTS_DIR, exist_ok=True)  

def analyze_load_data(processed_filename: str = None):
    # Defining the path to the data
    if processed_filename is None:
        processed_filename = os.path.join(PROCESSED_DIR, "processed_load_data.csv")
    
    # Loading data with timestamp parsing
    df = pd.read_csv(
        processed_filename,
        index_col="timestamp",
        parse_dates=True
    )
    # Converting an index to a datetime with UTC support
    df.index = pd.to_datetime(df.index, utc=True)
    
    print("=== Key Load Statistics ===")
    for col in df.columns:
        country_name = col.replace("_load_mw", "").title()
        max_val = df[col].max()
        max_date = df[df[col] == max_val].index[0].strftime("%Y-%m-%d %H:%M UTC")
        mean_val = df[col].mean()
        print(f"- {country_name}:")
        print(f"  • Average load: {mean_val:.0f} MW")
        print(f"  • Maximum load: {max_val:.0f} MW (date: {max_date})")
        print(f"  • Minimum load: {df[col].min():.0f} MW")
    
    # 1. Average daily load chart
    print("\nCreating a graph of average daily load...")
    df_daily = df.resample("D").mean()
    
    plt.figure()
    sns.lineplot(data=df_daily, x=df_daily.index, y="germany_load_mw", label="Germany", linewidth=1.5)
    sns.lineplot(data=df_daily, x=df_daily.index, y="hungary_load_mw", label="Hungary", linewidth=1.5)
    plt.title("Average daily load on the power grid (Germany and Hungary)")
    plt.xlabel("Date")
    plt.ylabel("Load, MW")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "daily_load.png"), dpi=150, bbox_inches="tight")
    plt.close()
    
    # 2. Hourly seasonality chart (average hourly load)
    print("Creating a time-based seasonality chart...")
    df_hourly = df.groupby(df.index.hour).mean()
    
    plt.figure()
    sns.barplot(data=df_hourly, x=df_hourly.index, y="germany_load_mw", alpha=0.7, label="Германия")
    sns.barplot(data=df_hourly, x=df_hourly.index, y="hungary_load_mw", alpha=0.7, label="Венгрия")
    plt.title("Average load by hours of the day")
    plt.xlabel("Hour (UTC)")
    plt.ylabel("Load, MW")
    plt.xticks(range(0, 24))
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "hourly_seasonality.png"), dpi=150, bbox_inches="tight")
    plt.close()
    
    print(f"The graphs are saved in the folder: {PLOTS_DIR}")

if __name__ == "__main__":
    analyze_load_data()
