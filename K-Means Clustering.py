def generate_data():
    data = []
    for i in range(100):
        x = (i * 17) % 10  # Generates pseudo-random values without `random`
        y = (i * 23) % 10
        data.append([x, y])
    return data

# Compute Euclidean distance manually
def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# Assign points to the nearest cluster
def assign_clusters(data, centroids):
    clusters = [[] for _ in centroids]
    for point in data:
        distances = []
        for centroid in centroids:
            distances.append(euclidean_distance(point, centroid))
        min_index = 0
        for i in range(1, len(distances)):  # Find minimum index manually
            if distances[i] < distances[min_index]:
                min_index = i
        clusters[min_index].append(point)
    return clusters

# Compute new centroids
def compute_centroids(clusters):
    centroids = []
    for cluster in clusters:
        if len(cluster) == 0:
            centroids.append([0, 0])  # Prevent division by zero
        else:
            sum_x = 0
            sum_y = 0
            for point in cluster:
                sum_x += point[0]
                sum_y += point[1]
            centroids.append([sum_x / len(cluster), sum_y / len(cluster)])
    return centroids

# K-Means Algorithm
def k_means(data, k=3, max_iterations=100):
    centroids = [data[i] for i in range(k)]  # Pick first k points as centroids

    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = compute_centroids(clusters)

        if new_centroids == centroids:
            break  # Stop if centroids don't change
        centroids = new_centroids

    return clusters, centroids

# Running K-Means
data = generate_data()
clusters, centroids = k_means(data, k=3)

# Printing results
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1} ({len(cluster)} points): {cluster}")
print(f"Final Centroids: {centroids}")

# The result is
# Cluster 1 (10 points): [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
# Cluster 2 (40 points): [[7, 3], [8, 2], [9, 1], [6, 4], [7, 3], [8, 2], [9, 1], [6, 4], [7, 3], [8, 2], [9, 1], [6, 4], [7, 3], [8, 2], [9, 1], [6, 4], [7, 3], [8, 2], [9, 1], [6, 4], [7, 3], [8, 2], [9, 1], [6, 4], [7, 3], [8, 2], [9, 1], [6, 4], [7, 3], [8, 2], [9, 1], [6, 4], [7, 3], [8, 2], [9, 1], [6, 4], [7, 3], [8, 2], [9, 1], [6, 4]]
# Cluster 3 (50 points): [[4, 6], [1, 9], [5, 5], [2, 8], [3, 7], [4, 6], [1, 9], [5, 5], [2, 8], [3, 7], [4, 6], [1, 9], [5, 5], [2, 8], [3, 7], [4, 6], [1, 9], [5, 5], [2, 8], [3, 7], [4, 6], [1, 9], [5, 5], [2, 8], [3, 7], [4, 6], [1, 9], [5, 5], [2, 8], [3, 7], [4, 6], [1, 9], [5, 5], [2, 8], [3, 7], [4, 6], [1, 9], [5, 5], [2, 8], [3, 7], [4, 6], [1, 9], [5, 5], [2, 8], [3, 7], [4, 6], [1, 9], [5, 5], [2, 8], [3, 7]]
# Final Centroids: [[0.0, 0.0], [7.5, 2.5], [3.0, 7.0]]
