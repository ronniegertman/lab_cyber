import json
import numpy as np
with open("traces.out", "r") as f:
    data = json.loads(f.read())
# Convert 2D array into Numpy for data processing
    traces = np.array(data["traces"])
# Labels are only available with the automation script.
# Use the line below in part 2.2 onward to access them.
# labels = data["labels"]
# Example data analysis
#average of data
print(len(traces[2]))
print("mean", traces.mean())
print("median", np.median(traces))