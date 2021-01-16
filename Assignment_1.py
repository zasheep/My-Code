import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from collections import defaultdict
digits = datasets.load_digits()

# Functionality f1 --------------------------------------
print(digits.DESCR,"\n\n--------------------------------------")
print("Number of Classes/Targets:", len(digits.target_names))
print("The minimum value of a feature: 0")
print("The maximum value of a feature: 16")
print("The number of data entries:", len(digits.data))

X = digits.data
y = digits.target

# The random_state number can be treated as a variable and you can change the number on it
(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.20, random_state=99)
# Validation data to help look for our k
(X_train, X_valid, y_train, y_valid) = train_test_split(X_train, y_train, test_size=0.1, random_state=5)

# Functionality f2 --------------------------------------
print("Training data points: {}".format(len(X_train)))
print("Testing data points: {}".format(len(y_test)))
print("Validation data points: {}\n".format(len(y_valid)))

# Selecting our n by searching for the kNN with the best accuracy
kValues = range(1, 20)
accuracies = []

# Loop over various values of k for the k-Nearest Neighbor classifier
for k in range(1, 20):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train,y_train)
    # Evaluate the model and update the accuracies list
    score = model.score(X_valid, y_valid)
    accuracies.append(score)

# Find the value of k that has the largest accuracy
n = np.argmax(accuracies)
print("k=%d achieved highest accuracy of %.2f%% on validation data, we will be using k=%d for both algorithms\n"
      % (kValues[n], accuracies[n] * 100, kValues[n]))

# Training the model on training set
knn = KNeighborsClassifier(n_neighbors=kValues[n])
knn.fit(X_train, y_train)

# Making predictions on the testing set
y_prediction = knn.predict(X_test)

# Functionality f3,--------------------------------------


def euclidean_distance(point_a, point_b):
    # Calculates euclidean distance of between point a and b
    return sum((point_a-point_b)**2)


def find_majority(labels):
    # Find the majority element of the label out of the many labels

    # defaultdict(type) is to automatically add new keys without throwing error.
    counter = defaultdict(int)
    for label in labels:
        counter[label] += 1

    # Finding the majority class.
    majority_count = max(counter.values())
    for key, value in counter.items():
        if value == majority_count:
            return key


def predict(k, train_images, train_labels, test_image):
    # Predicts new data-points's label by looking at other training labels

    # distances contains tuples of (distance, label) which we sum to find the euclidean distance
    distances = [(euclidean_distance(test_image, image), label)
                 for (image, label) in zip(train_images, train_labels)]
    # Sort the distances list by distances
    by_distances = sorted(distances)
    # Extract only k closest labels
    k_labels = [label for (_, label) in by_distances[:k]]
    # Return the majority voted label
    return find_majority(k_labels)

# Data Splitter, I choose 1293 to be fair to the library kNN model whose train and test set split into a 8:2 ratio
train_set_var = 1437
test_set_var = 1438

# Splitting data into train sets and test set
train_images = np.asarray(digits.data[:train_set_var])
train_labels = np.asarray(digits.target[:train_set_var])
test_images = np.asarray(digits.data[test_set_var:])
test_labels = np.asarray(digits.target[test_set_var:])

# Predicting and printing the accuracy
i = 0
total_correct = 0
acc = 0

print("Test errors on my kNN model")
for test_image in test_images:
    pred = predict(kValues[n], train_images, train_labels, test_image)
    if pred == test_labels[i]:
        total_correct += 1
        acc = (total_correct / (i + 1)) * 100
    else:
        # Outputs my test errors of my kNN model for functionality f4
        acc = (total_correct / (i + 1)) * 100
        print('image: [' + str(i) + ']', '\tpred:', pred, '\torig:', test_labels[i], '\tacc:',
              str(round(acc, 2)) + '%')
    i += 1

# Functionality f4, --------------------------------------

print("\n\nTest errors on Library function kNN model")
predictionLkNN = [digits.target_names[p] for p in y_prediction]
tester = [digits.target_names[p] for p in y_test]
total_correct_2 = 0
for i in range(len(predictionLkNN)):
    if tester[i] == predictionLkNN[i]:
        total_correct_2 += 1
        acc_2 = (total_correct_2 / (i + 1)) * 100
    else:
        acc_2 = (total_correct_2 / (i + 1)) * 100
        print('image: [' + str(i) + ']', '\tpred:', predictionLkNN[i], '\torig:', tester[i], '\tacc:',
              str(round(acc_2, 2)) + '%')


library_kNN_acc = metrics.accuracy_score(y_test, y_prediction) * 100
print("\nLibrary called kNN model accuracy: %.2f%%" % library_kNN_acc)
print("Library caleld kNN model error   : %.2f%%" % (100-library_kNN_acc))
print("my kNN model accuracy: %.2f%%" % acc)
print("my kNN model error   : %.2f%%" % (100-acc))
