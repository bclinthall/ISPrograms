import numpy as np
def evaluate(D, L, W, T):
    """
    :param D: Data. Each row is a feature vector
    :param L: correct labels for data
    :param W: Weight vector
    :param T: Numeric Threshold
    :return:
    """
    dots = D * W
    prediction = dots >= T

    correct_predictions = prediction == L
    overall_accuracy = sum(correct_predictions) / len(L)
    true_positives = prediction & L
    precision = sum(true_positives) / sum(prediction)
    recall = sum(true_positives) / sum(L)
    return {'overall_accuracy': overall_accuracy[0,0],
            'precision': precision[0,0],
            'recall': recall[0,0]}

D = np.matrix('1 1 0 4; 2 0 1 1; 2 3 0 0; 0 2 3 1; 4 0 2 0; 3 0 1 3')
L = np.matrix('1; 1; 0; 0; 0; 0')
W = np.matrix('1; 2; 1; 2')
T = 9
evaluate(D, L, W, T)

def evaluate2(D, L, W, T):
    """
    :param D: Data. Each row is a feature vector
    :param L: correct labels for data
    :param W: Weight vector
    :param T: Numeric Threshold
    :return:
    """


    dots = D * W
    prediction = dots >= T

    correct_predictions = prediction == L
    overall_accuracy = sum(correct_predictions) / len(L)
    true_positives = prediction & L
    precision = sum(true_positives) / sum(prediction)
    recall = sum(true_positives) / sum(L)

    return np.stack([overall_accuracy, precision, recall])

W = np.matrix('1 0; 2 0; 1 0; 2 1')
T = np.matrix('9 2')
evaluate2(D, L, W, T)
