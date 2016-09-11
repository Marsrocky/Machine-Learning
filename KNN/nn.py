import numpy as np

class NearestNeighbor(object):
	"""KNN train and predict"""
	def __init__(self):
		pass

	def train(self, X, y):
		"""X is N x D and y is 1-d of size N"""
		self.Xtr = X
		self.ytr = y

	def predict(self, Xte):
		""" X is N x D to be predicted """
		num = Xte.shape[0]
		Ypre = np.zeros(num, dtype = self.ytr.dtype)

		# loop over all rows
		for i in xrange(num):
			distances = np.sum(np.abs(self.Xtr-Xte[i,:]), axis=1)
			min_index = np.argmin(distances)
			Ypre[i] = self.ytr[min_index]
			print 'Item %d is processed...' % i

		return Ypre