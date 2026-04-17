import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# LOAD DATA
# ----------------------------
data = pd.read_csv("cities.csv")
X = data.values  # shape (n,2)

# ----------------------------
# HELPER FUNCTIONS
# ----------------------------
def initialize_centroids(X, k=3):
    indices = np.random.choice(len(X), k, replace=False)
    return X[indices]

def assign_clusters(X, centroids):
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

def compute_ssd(X, centroids, labels):
    ssd = 0
    for i in range(len(X)):
        ssd += np.sum((X[i] - centroids[labels[i]])**2)
    return ssd

# ----------------------------
# METHOD A: GRADIENT DESCENT
# ----------------------------
def gradient_descent_kmeans(X, k=3, max_iters=100):
    centroids = initialize_centroids(X, k)

    for _ in range(max_iters):
        labels = assign_clusters(X, centroids)

        new_centroids = np.array([
            X[labels == i].mean(axis=0) if len(X[labels == i]) > 0 else centroids[i]
            for i in range(k)
        ])

        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    ssd = compute_ssd(X, centroids, labels)
    return centroids, labels, ssd

# ----------------------------
# METHOD B: NEWTON-RAPHSON
# ----------------------------
def newton_method_kmeans(X, k=3, max_iters=50):
    centroids = initialize_centroids(X, k)

    for _ in range(max_iters):
        labels = assign_clusters(X, centroids)

        new_centroids = []

        for i in range(k):
            cluster_points = X[labels == i]

            if len(cluster_points) == 0:
                new_centroids.append(centroids[i])
                continue

            # Gradient
            gradient = np.sum(cluster_points - centroids[i], axis=0)

            # Hessian
            H = 2 * len(cluster_points) * np.eye(2)

            # Newton update
            update = np.linalg.inv(H).dot(gradient)
            new_mu = centroids[i] - update

            new_centroids.append(new_mu)

        new_centroids = np.array(new_centroids)

        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    ssd = compute_ssd(X, centroids, labels)
    return centroids, labels, ssd

# ----------------------------
# RUN BOTH METHODS
# ----------------------------
centroids_gd, labels_gd, ssd_gd = gradient_descent_kmeans(X)
centroids_nr, labels_nr, ssd_nr = newton_method_kmeans(X)

# ----------------------------
# PRINT RESULTS
# ----------------------------
print("========== RESULTS ==========\n")

print("Gradient Descent SSD:", ssd_gd)
print("Gradient Descent Airports:\n", centroids_gd)

print("\nNewton-Raphson SSD:", ssd_nr)
print("Newton-Raphson Airports:\n", centroids_nr)

# ----------------------------
# VISUALIZATION
# ----------------------------
def plot_clusters(X, labels, centroids, title):
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200)
    plt.title(title)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.show()

plot_clusters(X, labels_gd, centroids_gd, "Gradient Descent Clusters")
plot_clusters(X, labels_nr, centroids_nr, "Newton-Raphson Clusters")
