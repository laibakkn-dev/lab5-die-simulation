import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
rolls = np.random.randint(1, 7, size=1000)

# (a) first 10 rolls
print("First 10 rolls:", rolls[:10])

# (b) count each face
faces, counts = np.unique(rolls, return_counts=True)

# (c) empirical vs theoretical probability
print(f"{'Face':<6}{'Count':<8}{'Empirical P':<14}{'Theoretical P'}")
for face, count in zip(faces, counts):
    print(f"{face:<6}{count:<8}{count/1000:<14.3f}{1/6:.4f}")

# (d) histogram
plt.figure(figsize=(6, 4))
plt.hist(rolls, bins=np.arange(0.5, 7.5, 1), rwidth=0.8,
         color="steelblue", edgecolor="black")
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("1000 Rolls of a Fair Die")
plt.xticks(range(1, 7))
plt.tight_layout()
plt.savefig("die_rolls.png")
print("Saved die_rolls.png")