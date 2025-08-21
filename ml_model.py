import numpy as np
from sklearn.tree import DecisionTreeClassifier


X = np.array([[i] for i in range(1, 10001)])   
y = np.array([i % 2 for i in range(1, 10001)]) 


model = DecisionTreeClassifier()
model.fit(X, y)

print("Model trained successfully ✅")
print("Training Accuracy:", model.score(X, y))


while True:
    try:
        num = int(input("\nEnter a number (or -1 to exit): "))
        if num == -1:
            print("Exiting...")
            break
        pred = model.predict([[num]])[0]
        print(f"{num} → {'Odd' if pred == 1 else 'Even'}")
    except ValueError:
        print("⚠ Please enter a valid integer.")
