# Importing necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

# Initializing KMeans with 3 clusters
kmeans = KMeans(n_clusters=3)

# Fitting the model and predicting clusters
df['Cluster'] = kmeans.fit_predict(df[['Height', 'Weight', 'Age']])

# Displaying the DataFrame with cluster assignments
print("\nCluster assignments:\n", df)

# Plotting the clusters using the first two features (Height, Weight)
plt.scatter(df['Height'], df['Weight'], c=df['Cluster'], cmap='viridis', s=100)
plt.title('KMeans Clustering')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()
