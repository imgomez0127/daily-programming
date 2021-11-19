import numpy as np
import pandas as pd
import scipy.stats


def preprocess_data(data):
    return np.array(data.drop(columns=[4]))


class GMM:

    def __init__(self, feature_size, num_classes=3):
        self.means = np.random.random((num_classes, feature_size))
        self.covs = np.array([np.identity(feature_size)
                              for _ in range(num_classes)])
        self.num_classes = num_classes
        self.pis = np.random.random(num_classes)

    def expectation_step(self, iris_data):
        gammas = []
        for sample in iris_data:
            normalization_term = 0
            sample_gammas = np.zeros((self.num_classes))
            for j in range(self.num_classes):
                normal_dist = scipy.stats.multivariate_normal(
                    mean=self.means[j], cov=self.covs[j])
                # Compute numerator of GMM probability
                prob = normal_dist.pdf(sample)
                prob *= self.pis[j]
                sample_gammas[j] = prob
                normalization_term += prob
            gammas.append(sample_gammas/normalization_term)
        return np.array(gammas)

    def predict(self, data_point):
        """Hard assigns each data point to a class.

        Assigns each data point to a class based on which cluster provides the
        highest probability. e.g. given probabilities [0.2, 0.45, 0.35] the
        model will assign it to the 1st cluster.
        """
        if len(data_point.shape) > 2:
            raise ValueError()
        if len(data_point.shape) != 2:
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
            for j, gamma in enumerate(gammas[i]):
                means[j] += gamma*sample
                std = (sample-self.means[j]).reshape(1, -1)
                covs[j] += gamma*(std.T@std)
        means = means/assignment_counts[:, None]
        covs = covs/assignment_counts[:, None, None]
        return means, covs, pis

    def train(self, iris_data, epochs=1000):
        for _ in range(epochs):
            gammas = self.expectation_step(iris_data)
            means, covs, pis = self.maximization_step(iris_data, gammas)
            self.means = means
            self.covs = covs
            self.pis = pis

    def __call__(self, data_point):
        return self.predict(data_point)


def main():
    iris_data = preprocess_data(pd.read_csv('iris.data', header=None))
    GMM_MODEL = GMM(iris_data.shape[1])
    GMM_MODEL.train(iris_data)
    print(GMM_MODEL.predict(iris_data[0:3]))
    print(GMM_MODEL.predict(iris_data[-3:-1]))

if __name__ == '__main__':
    main()
