import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

np.random.seed(42)

# Generate sample student data:
# study hours, attendance percentage, internal marks
X = np.column_stack([
    np.random.uniform(0, 10, 500),
    np.random.uniform(40, 100, 500),
    np.random.uniform(0, 100, 500)
])

# Generate Pass/Fail labels using sample rules
y = (
    (X[:, 0] >= 4) &
    (X[:, 1] >= 65) &
    (X[:, 2] >= 40)
).astype(int)

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

joblib.dump(model, "student_model.pkl")
print("Model trained and saved successfully!")
