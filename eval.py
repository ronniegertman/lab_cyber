import json
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def eval():
	y_pred_full, y_test_full = [], []

	# Re-train 10 times in order to reduce effects of randomness
	for i in range(10):
		### TODO: Exercise 2-4
		### 1. Load data from traces file
		labels, traces = [], []
		with open("traces.out", "r") as f:
			data = json.loads(f.read())
			# Convert 2D array into Numpy for data processing
			traces = np.array(data["traces"])
			labels = np.array(data["labels"])
		print(len(traces[0]))

		### 2. Split data into X_train, X_test, y_train, y_test with train_test_split
		x_train, x_test, y_train, y_test = train_test_split(traces, labels, test_size=0.2)
		model = RandomForestClassifier()

		### 3. Train classifier with X_train and y_train
		model.fit(x_train, y_train)
		### 4. Use classifier to make predictions on X_test. Save the result to a variable called y_pred
		y_pred = model.predict(x_test)

		# Do not modify the next two lines
		y_test_full.extend(y_test)
		y_pred_full.extend(y_pred)

	### TODO: Exercise 2-4 (continued)
	### 5. Print classification report using y_test_full and y_pred_full
	accuracy = accuracy_score(y_test_full, y_pred_full)
	print(f"Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
	eval()
