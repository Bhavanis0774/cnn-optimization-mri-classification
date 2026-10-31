# Batch Normalization in CNN Models

## 1. Introduction

Batch Normalization is a technique used in deep neural networks to normalize intermediate activations during training. It helps stabilize training and can improve convergence.

In this project, Batch Normalization is studied as an optimization technique for CNN-based MRI brain tumor classification.

## 2. Objective

The objectives of this experiment are:

- Investigate the effect of Batch Normalization on CNN training.
- Compare model performance before and after optimization.
- Evaluate training, validation, and test accuracy.
- Study its contribution to training stability.

## 3. Implementation

Batch Normalization is incorporated into the DenseNet-121 classification model after selected fully connected layers.

The model also uses dropout regularization, the Adam optimizer, learning-rate reduction, and early stopping.

## 4. Experimental Results

The following results were recorded for the DenseNet-121 experiment.

| Metric | Without Optimization | With Batch Normalization |
|---|---:|---:|
| Training Accuracy | 90% | 94% |
| Validation Accuracy | 88% | 89.45% |
| Test Accuracy | 88% | 90% |
| Model Parameters | 7,432,654 | Not specified |

## 5. Results Analysis

The recorded results show improvements in all three reported accuracy metrics after optimization.

- Training accuracy increased from 90% to 94%.
- Validation accuracy increased from 88% to 89.45%.
- Test accuracy increased from 88% to 90%.

These results indicate improved classification performance in the reported experiment.

## 6. Conclusion

Batch Normalization can help stabilize neural network training and improve classification performance. Its effectiveness depends on the model architecture, dataset, and training configuration.
