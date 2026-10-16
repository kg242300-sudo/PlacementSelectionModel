import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")

# Create a figure with two subplots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 1. Boxplot of CGPA vs Placement Status
sns.boxplot(
    data=df,
    x="Placed",
    y="CGPA",
    ax=axes[0],
    palette="Set2",
    hue="Placed",
    legend=False
)
axes[0].set_title("CGPA Distribution (Boxplot)", fontsize=14)
axes[0].set_xticks([0, 1])
axes[0].set_xticklabels(["Not Placed", "Placed"])
axes[0].set_xlabel("Placement Status", fontsize=12)
axes[0].set_ylabel("CGPA", fontsize=12)

# 2. KDE Plot of CGPA vs Placement Status
sns.kdeplot(
    data=df,
    x="CGPA",
    hue="Placed",
    fill=True,
    common_norm=False,
    palette="Set2",
    alpha=0.5,
    linewidth=2,
    ax=axes[1]
)
axes[1].set_title("CGPA Density Estimate (KDE Plot)", fontsize=14)
axes[1].set_xlabel("CGPA", fontsize=12)
axes[1].set_ylabel("Density", fontsize=12)
axes[1].legend(title="Placement", labels=["Placed", "Not Placed"])

plt.suptitle("CGPA Distribution of Placed vs. Not Placed Students", fontsize=16, y=1.02)
plt.tight_layout()
plt.show()
