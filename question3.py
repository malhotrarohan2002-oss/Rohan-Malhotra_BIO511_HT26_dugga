import sys
import pandas as pd
import matplotlib.pyplot as plt

input_file = sys.argv[1]
output_file = sys.argv[2]

data = pd.read_csv(input_file)

plt.scatter(data["position_mb"],data["log2_ratio"])
plt.xlabel("position_mb")
plt.ylabel("log2_ratio")
plt.title("Log2_ratio vs Position")
plt.savefig(output_file)
plt.show()