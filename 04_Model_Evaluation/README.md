# Model Evaluation for MRI Brain Tumor Classification

## 1. Introduction

Model evaluation is an important stage of the CNN optimization research project. It measures how accurately a model classifies MRI images and helps compare the performance of different models and optimization techniques.

The project focuses on classifying MRI images into four categories:

- Glioma
- Meningioma
- No Tumor
- Pituitary

## 2. Evaluation Metrics

### 2.1 Accuracy

Accuracy measures the proportion of correctly classified images among all evaluated images.

Accuracy = Correct Predictions / Total Predictions

### 2.2 Precision

Precision measures the proportion of correct positive predictions among all positive predictions for a class.

Precision = True Positives / (True Positives + False Positives)

### 2.3 Recall

Recall measures the proportion of actual positive samples correctly identified for a class.

Recall = True Positives / (True Positives + False Negatives)

### 2.4 F1-Score

The F1-score is the harmonic mean of precision and recall.

F1-Score = 2 × (Precision × Recall) / (Precision + Recall)

### 2.5 Confusion Matrix

A confusion matrix compares actual class labels with predicted class labels. It helps identify which tumor categories are correctly classified and which categories are confused with one another.

## 3. Dataset Splits

The project uses separate training and validation directories.

- **Training set:** Used to learn model parameters.
- **Validation set:** Used to monitor model performance and guide training decisions.
- **Test set:** Used for final evaluation on independent data, when available.

Validation accuracy and test accuracy are reported separately.

## 4. DenseNet-121 Evaluation

The DenseNet-121 training script evaluates the model using the validation dataset.

It generates the following outputs:

- Training and validation accuracy curves
- Training and validation loss curves
- Confusion matrix
- Classification report
- Model parameter summary

These outputs help analyze model learning, classification performance, and potential errors.

## 5. Optimization Comparison

Model evaluation is used to compare the baseline CNN with optimized versions.

The comparison considers:

- Classification accuracy
- Precision, recall, and F1-score
- Number of model parameters
- Model size
- Inference latency, when measured

## 6. Recorded Experimental Results

The following results were recorded for selected DenseNet-121 experiments.

| Experiment | Training Accuracy | Validation Accuracy | Test Accuracy |
|---|---:|---:|---:|
| Batch Normalization — Without Optimization | 90% | 88% | 88% |
| Batch Normalization — With Optimization | 94% | 89.45% | 90% |
| Tensor Decomposition — Before | 99.58% | 99.61% | 100% |
| Tensor Decomposition — After | 99.51% | 99.61% | 100% |

## 7. Conclusion

Model evaluation provides a systematic way to compare CNN architectures and optimization techniques. Accuracy, precision, recall, F1-score, confusion matrices, and model complexity together provide a more complete assessment than accuracy alone.
