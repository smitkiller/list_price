# import the necessary packages
import numpy as np
import csv
class Searcher:
	def __init__(self, features_list):
		# store our index path
		self.features_list = features_list
	def search(self, queryFeatures, limit = 3):
		results = {}

		for line in self.features_list:
			data_list = line.features.split(',')
			features = [float(x) for x in data_list]
			d = self.chi2_distance(features, queryFeatures)

			# print(features, queryFeatures)
						
			results[line.name] = d, line.id

		results = sorted([((v, i), k) for (k, (v, i)) in results.items()])

		return results[:limit]


	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
		# return the chi-squared distance
		# d ค่าความคลาดเคลื่อน
		return d
