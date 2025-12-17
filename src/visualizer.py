import matplotlib.pyplot as plt
import os

# Ensure the output folder exists
os.makedirs("output/plots", exist_ok=True)

def plot_trend_by_category(df):
    categories = df["round_type"].unique()

    for category in categories:
        subset = df[df["round_type"] == category]

        plt.figure(figsize=(10, 5))
        plt.plot(subset["date"], subset["min_crs_score"], marker='o')
        plt.xlabel("Date")
        plt.ylabel("Minimum CRS Score")
        plt.title(f"CRS Score Trend - {category}")
        plt.tight_layout()

        # Safe file name: lowercase + underscores
        filename = f"output/plots/crs_trend_{category.lower().replace(' ', '_')}.png"
        plt.savefig(filename)
        plt.close()
        print(f"Saved plot for {category}: {filename}")
