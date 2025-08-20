# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic customer engagement data
np.random.seed(42)
data = pd.DataFrame({
    "Website_Visits": np.random.randint(100, 1000, 50),
    "Email_Clicks": np.random.randint(50, 500, 50),
    "Social_Interactions": np.random.randint(20, 400, 50),
    "Purchases": np.random.randint(5, 100, 50),
    "Support_Tickets": np.random.randint(1, 50, 50)
})

# Compute correlation matrix
corr = data.corr()

# Create heatmap
plt.figure(figsize=(8, 8))  # ensures 512x512 when saved with dpi=64
sns.heatmap(corr, annot=True, cmap="RdYlGn", vmin=-1, vmax=1, square=True,
            linewidths=0.5, cbar_kws={"shrink": 0.8})

plt.title("Customer Engagement Correlation Matrix", fontsize=16, pad=20)

# Save exactly 512x512
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
