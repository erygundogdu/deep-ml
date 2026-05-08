
import numpy as np
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	def dist(point, centroid):
		point = np.array(point)
		centroid = np.array(centroid)
		dst = ((point - centroid) ** 2).sum()
		return np.sqrt((dst))
	centroids = initial_centroids.copy()
	for _ in range(max_iterations):
		dst_lst = []

		for point in points:
			sub_dst_lst = []
			for i in range(k):
				dst = dist(point, centroids[i])
				sub_dst_lst.append(dst)
			dst_lst.append(sub_dst_lst)
		assignments = []
		for sub in dst_lst:
			assignments.append(np.argmin(sub))
		## [[7,8],[2,1]] , [1,0]
		clusters = []
		for i in range(k):
			clusters.append([])

		for point, cluster_idx in zip(points, assignments):
			clusters[cluster_idx].append(point)
		new_centroids = []
		for i in range(k):
			if len(clusters[i]) == 0:
				new_centroids.append(centroids[i])
			else:
				cluster_np = np.array(clusters[i])
				new_centroid = tuple(cluster_np.mean(axis=0))
				new_centroids.append(new_centroid)
		centroids = new_centroids
	return centroids


	
			

	


	return final_centroids