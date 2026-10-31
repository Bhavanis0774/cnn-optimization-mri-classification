# Confusion Matrix for MRI Brain Tumor Classification

## 1. Introduction

A confusion matrix is used to evaluate the classification performance of a CNN model by comparing actual class labels with predicted class labels.

In this project, it helps analyze the classification of MRI images into four categories:

- Glioma
- Meningioma
- No Tumor
- Pituitary

## 2. Structure

The confusion matrix contains four rows and four columns:

- Rows represent the actual classes.
- Columns represent the predicted classes.
- Diagonal values represent correct predictions.
- Off-diagonal values represent incorrect predictions.

## 3. Example

The following is an illustrative confusion matrix using sample values. It is not the actual result of the trained MRI classification model.

| Actual / Predicted | Glioma | Meningioma | No Tumor | Pituitary |
|---|---:|---:|---:|---:|
| Glioma | 45 | 2 | 1 | 2 |
| Meningioma | 1 | 46 | 2 | 1 |
| No Tumor | 0 | 1 | 48 | 1 |
| Pituitary | 2 | 1 | 1 | 46 |

## 4. Interpretation

A high value on the diagonal indicates that the model correctly classified more images belonging to that class.

Off-diagonal values help identify misclassifications. For example, an image belonging to the Glioma class that is predicted as Meningioma contributes to the corresponding off-diagonal cell.

## 5. Implementation

The project's Python evaluation script uses:

- `sklearn.metrics.confusion_matrix` to calculate the matrix.
- `seaborn.heatmap` to visualize the results.
- Matplotlib to save the confusion matrix as an image.

The generated figure is saved as `confusion_matrix.png`.

## 6. Importance

The confusion matrix helps identify class-specific weaknesses that may not be apparent from overall accuracy alone.

It supports comparisons between baseline and optimized CNN models.

## 7. Conclusion

Confusion matrix analysis provides a detailed view of classification errors and correct predictions across all four MRI brain image categories. Actual experimental results should be generated using predictions from the trained model.
