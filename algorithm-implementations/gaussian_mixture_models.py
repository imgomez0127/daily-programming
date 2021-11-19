import numpy as np
import pandas as pd
import scipy.stats
import sklearn.mixture


def preprocess_data(data):
    return np.array(data.drop(columns=[4]))


class GMM:

    def __init__(self, feature_size, num_classes=3):
        self.means = np.random.random((num_classes, feature_size))
        self.covs = np.array([np.identity(feature_size)
                              for _ in range(num_classes)])
        self.num_classes = num_classes
        self.pis = np.array([1/num_classes for _ in range(num_classes)])

    def expectation_step(self, iris_data):
        """Computes the expectation step of the EM Algorithm

        This computes the expectation step where we compute the
        P(k|x) for each item in the dataset. This is used to find
        out how likely a data point is to be a part of a cluster.
        """
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

    def maximization_step(self, iris_data, gammas):
        """Performs the maximization step of the EM algorithm

        This computes the new values of each parameter for the
        GMM model. It re-estimates the means, covariances, and
        mixing coefficients of the GMM using the estimations of
        P(k|x) in the expectation step.
        """
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

    def train(self, iris_data, epochs=100):
        for _ in range(epochs):
            gammas = self.expectation_step(iris_data)
            means, covs, pis = self.maximization_step(iris_data, gammas)
            self.means = means
            self.covs = covs
            self.pis = pis

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

    def soft_predict(self, data_point):
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
        return gammas

    def __call__(self, data_point):
        return self.predict(data_point)


def main():
    iris_data = preprocess_data(pd.read_csv('iris.data', header=None))
    GMM_MODEL = GMM(iris_data.shape[1])
    GMM_MODEL.train(iris_data)
    predicted_classes = GMM_MODEL.predict(iris_data)
    np.savetxt("classes.csv", predicted_classes, delimiter=",")
    print(GMM_MODEL.soft_predict(iris_data[0:3]))
    print("Means")
    print(GMM_MODEL.means)
    print("Covs")
    print(GMM_MODEL.covs)
    print("Pis")
    print(GMM_MODEL.pis)
    SKLEARN_GMM = sklearn.mixture.GaussianMixture(n_components=3, init_params='random').fit(iris_data)
    print("Means")
    print(SKLEARN_GMM.means_)
    print("Covs")
    print(SKLEARN_GMM.covariances_)
    print("Pis")
    print(SKLEARN_GMM.weights_)
    predicted_classes = SKLEARN_GMM.predict(iris_data)
    np.savetxt("sklearn_classes.csv", predicted_classes, delimiter=",")


if __name__ == '__main__':
    main()
