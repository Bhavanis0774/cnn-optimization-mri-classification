# DenseNet-121 for MRI Brain Tumor Classification

## 1. Project Overview

This project investigates optimization techniques for Convolutional Neural Networks (CNNs) used in MRI brain tumor classification.

DenseNet-121 is studied as a baseline architecture, and different optimization methods are evaluated to understand their effects on classification accuracy and model complexity.

The project focuses on the following four classes:

- Glioma
- Meningioma
- No Tumor
- Pituitary

## 2. Objectives

- Study DenseNet-121 for MRI brain tumor classification.
- Evaluate the baseline model.
- Investigate batch normalization and other optimization techniques.
- Study parameter reduction using tensor decomposition and pruning.
- Compare model performance before and after optimization.
- Analyze the trade-off between classification accuracy and model complexity.

## 3. Dataset and Preprocessing

The project uses brain MRI images belonging to four classes: Glioma, Meningioma, No Tumor, and Pituitary.

The image preprocessing configuration includes resizing images to 224 × 224 pixels for DenseNet-121.

The preprocessing workflow includes image loading, resizing, normalization, label preparation, and dataset splitting.

## 4. DenseNet-121 Architecture

DenseNet-121 is a convolutional neural network that uses dense connections between layers to encourage feature reuse and improve information propagation.

Its principal components include:

- Initial convolution and pooling layers.
- Dense blocks.
- Transition layers.
- Global average pooling.
- A classification layer.

The final classification layer is configured for four output classes.

## 5. Optimization Techniques

The project investigates the following techniques:

### Batch Normalization
Evaluates the effect of batch normalization on training, validation, and test performance.

### Weight Pruning
Reduces or masks selected model weights according to a pruning criterion.

### Network and Layer Pruning
Investigates the removal of selected model components to reduce complexity.

### Quantization
Studies reduced numerical precision to potentially decrease model storage and computational requirements.

### Depthwise Convolution
Investigates depthwise convolution as a way to reduce computation in suitable convolutional architectures.

### Tensor Decomposition
Approximates model weights using a lower-complexity representation to reduce parameter count.

### Knowledge Distillation
Transfers predictive information from a teacher model to a student model.

## 6. Experimental Results

### 6.1 Batch Normalization

The following results were reported in the project experiment comparison:

| Metric | Without Optimization | With Batch Normalization |
|---|---:|---:|
| Training Accuracy | 90% | 94% |
| Validation Accuracy | 88% | 89.45% |
| Test Accuracy | 88% | 90% |
| Reported Parameters | 7,432,654 | Not specified |

The reported test accuracy increased from 88% to 90% in this comparison.

### 6.2 Tensor Decomposition

The following results were recorded for the tensor decomposition experiment:

| Metric | Before Decomposition | After Decomposition |
|---|---:|---:|
| Training Accuracy | 99.58% | 99.51% |
| Validation Accuracy | 99.61% | 99.61% |
| Test Accuracy | 100% | 100% |
| Number of Parameters | 6,957,956 | 5,363,188 |

The reported parameter count decreased from 6,957,956 to 5,363,188, while the recorded test accuracy remained at 100%.

The parameter reduction is approximately 22.92%.

### 6.3 Pruning

The project comparison documents also report the following parameter figures:

| Metric | Reported Value |
|---|---:|
| Original Parameter Count | 6,957,956 |
| Pruned Parameter Count | 2,087,386 |
| Remaining Effective Parameters | 4,870,570 |

These values are retained as reported in the project material. The precise pruning configuration and interpretation of these parameter counts should be checked against the corresponding experiment before drawing further conclusions.

## 7. Model Evaluation

The project evaluates CNN models using classification metrics and model-complexity measurements.

The evaluation metrics include:

- Training accuracy.
- Validation accuracy.
- Test accuracy.
- Precision.
- Recall.
- F1-score.
- Confusion matrix.
- Model parameter count.

Model size and inference time are also useful for assessing deployment efficiency when measurements are available.

## 8. Interpretation

The recorded batch normalization experiment shows an increase in test accuracy from 88% to 90%.

The tensor decomposition experiment reports a reduction in parameter count while maintaining the reported accuracy values.

These results suggest that optimization methods should be evaluated using both predictive performance and model complexity.

The results from different experiments should not be compared directly unless the dataset split, evaluation procedure, and experimental configuration are consistent.

## 9. Technologies

The project uses deep learning and scientific computing tools, including:

- Python.
- PyTorch.
- Jupyter Notebook.
- NumPy.
- Matplotlib.
- scikit-learn.

The final dependency list should match the actual project implementation.

## 10. Conclusion

DenseNet-121 provides a baseline for evaluating CNN optimization techniques in MRI brain tumor classification.

The reported experiments examine batch normalization, tensor decomposition, and pruning-related parameter reduction.

The final comparison of optimization methods should consider classification performance, parameter count, model storage, and inference efficiency.
