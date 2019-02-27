#coding=utf-8
 
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

data = datasets.load_digits()

images_and_labels = list(zip(data.images, data.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index+1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Trainning %i' % label)

n_sample = len(data.images)

d = data.images.reshape((n_sample, -1))

classifier = svm.SVC(gamma=0.001)

classifier.fit(d[:n_sample//2], data.target[:n_sample//2])

excepted = data.target[n_sample//2:]
predicted = classifier.predict(d[n_sample//2:])

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(excepted, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(excepted, predicted))

images_and_predictions = list(zip(data.images[n_sample // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()
