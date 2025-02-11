# Generate dataset manually
def generate_dataset():
    data = []
    for i in range(100):
        x = (i * 19) % 10  # Pseudo-random pattern without `random`
        y = (i * 29) % 10
        label = 1 if (x + y) > 10 else 0
        data.append((x, y, label))
    return data

# Compute Euclidean distance manually
def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# KNN Algorithm
def knn(train_data, test_point, k=3):
    distances = []
    for i in range(len(train_data)):
        x, y, label = train_data[i]
        distance = euclidean_distance((x, y), test_point)
        distances.append((distance, label))

    # Manually sort based on distance
    for i in range(len(distances) - 1):
        for j in range(i + 1, len(distances)):
            if distances[i][0] > distances[j][0]:
                distances[i], distances[j] = distances[j], distances[i]

    nearest_neighbors = distances[:k]

    # Majority vote
    label_counts = {0: 0, 1: 0}
    for _, label in nearest_neighbors:
        label_counts[label] += 1

    return 0 if label_counts[0] > label_counts[1] else 1

# Splitting dataset into training and testing
dataset = generate_dataset()
train_data = dataset[:80]
test_data = dataset[80:]

# Evaluate KNN
correct = 0
for i in range(len(test_data)):
    x, y, actual_label = test_data[i]
    predicted_label = knn(train_data, (x, y), k=3)
    correct += (predicted_label == actual_label)

accuracy = correct / len(test_data)
print(f"KNN Accuracy: {accuracy:.2f}")

# The result is
# KNN Accuracy: 1.00
