import numpy as np
import pandas as pd
import scipy.stats


def preprocess_data(data):
    return data


class GMM:

    def __init__(self, feature_size, num_classes=3):
        self.means = np.random.random((feature_size, num_classes))
        self.covs = np.array([np.identity(feature_size)
                              for _ in range(num_classes)])
        self.num_classes = num_classes
        self.pis = np.random.random((1, num_classes))

    def expectation_step(self, iris_data):
        gammas = []
        for sample in iris_data:
            normalization_term = 0
            sample_gammas = np.zeros((self.num_classes))
            for j in range(self.num_classes):
                normal_dist = scipy.stats.multivariate_normal(
                    mean=self.means[j], covs=self.covs[j])
                # Compute numerator of GMM probability
                prob = normal_dist.pdf(sample)
                prob *= self.pis[j]
                sample_gammas[j] = prob
                normalization_term += prob
            gammas.append(sample_gammas/normalization_term)
        return np.array(gammas)

    def predict(self, data_point):
        if data_point.shape > 2:
            raise ValueError()
        if data_point.shape != 2:
            data_point.reshape((1, -1))
        gammas = self.expectation_step(data_point)
        return np.argmax(gammas, axis=1)

    def maximization_step(self, iris_data, gammas):
        assignment_counts = np.array([sum(gammas[:, i])
                                      for i in range(self.num_classes)])
        means = np.zeros(self.means.shape)
        covs = np.zeros(self.covs.shape)
        pis = assignment_counts/len(iris_data)
        for i, sample in enumerate(iris_data):
            for j in range(len(gammas)):
                means[j] += gammas[i][j]*sample
                std = (sample-self.means[j])
                covs[j] += gammas[i][j]*(std.T@std)
        means = means/assignment_counts[:, None]
        covs = covs/assignment_counts[:, None]
        return means, covs, pis

    def train(self, iris_data, epochs=100):
        for _ in range(epochs):
            gammas = self.expectation_step(iris_data)
            means, covs, pis = self.maximization_step(iris_data, gammas)
            self.means = means
            self.covs = covs
            self.pis = pis

    def __call__(self, data_point):
        return self.predict(data_point)


def main():
    iris_data = preprocess_data(pd.read_csv('iris.data'))
    GMM_MODEL = GMM(iris_data.shape[1])
    GMM_MODEL.train(iris_data)
