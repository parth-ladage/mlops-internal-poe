
import pandas as pd
from sklearn.datasets import load_iris
from evidently import Report
from evidently.presets import DataDriftPreset

# Load the original Iris dataset
iris = load_iris(as_frame=True)

reference_data = iris.data.copy()


reference_data.columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]

# Create current data by changing feature distributions
current_data = reference_data.copy()

# Introduce significant data drift
current_data["sepal_length"] += 2.0
current_data["sepal_width"] += 1.5
current_data["petal_length"] += 2.5
current_data["petal_width"] += 1.0

# Generate the data drift report
report = Report([
    DataDriftPreset()
])

my_report = report.run(
    reference_data=reference_data,
    current_data=current_data
)

# Save the report as HTML
my_report.save_html("iris_drift_report.html")

print("Iris data drift report generated successfully!")
print("Open iris_drift_report.html to view the results.")
