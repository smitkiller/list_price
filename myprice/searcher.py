# import the necessary packages
import numpy as np
import csv
class Searcher:
	def __init__(self, indexPath):
		# store our index path
		self.indexPath = indexPath
	def search(self, queryFeatures, limit = 3):
		# initialize our dictionary of results
		# print(queryFeatures)
		results = {}
		# open the index file for reading
		with open(self.indexPath) as f:
			# initialize the CSV reader
			reader = csv.reader(f)

			# loop over the rows in the index
			for row in reader:
				# print(row)
				# parse out the image ID and features, then compute the
				# chi-squared distance between the features in our index
				# and our query features
				if row[1] != '':
					features = [float(x) for x in row[2:]]
					# if row[0] == 'dataset\\girl.png':
						# print(features)
						# print(queryFeatures)
					d = self.chi2_distance(features, queryFeatures)
					# print(d)
					# now that we have the distance between the two feature
					# vectors, we can udpate the results dictionary -- the
					# key is the current image ID in the index and the
					# value is the distance we just computed, representing
					# how 'similar' the image in the index is to our query
					results[row[1]] = d, row[0]
					# print(results)
			# close the reader
			f.close()
		# print("aaaaa",results.items())
		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		# results = sorted([(float(str(v)[:5]), k) for (k, v) in results.items()])
		results = sorted([((v, i), k) for (k, (v, i)) in results.items()])
		# return our (limited) results

		# print("bbbbb",results)
		return results[:limit]


	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
		# return the chi-squared distance
		# d ค่าความคลาดเคลื่อน
		return d
