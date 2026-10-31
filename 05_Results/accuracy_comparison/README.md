# Accuracy Comparison of CNN Models

## 1. Overview

This section documents the accuracy comparison conducted during the research project, **"Study of Optimization Techniques and Their Implementation on CNN Models for Image Classification."**

The objective was to evaluate CNN models for MRI brain tumor classification and identify the model that provides the best classification accuracy.

## 2. Selected CNN Model

**DenseNet-121 was selected as the best-performing CNN model based on the classification accuracy obtained in this study.**

DenseNet-121 uses dense connections between layers, allowing feature information to be reused throughout the network. This characteristic makes it suitable for extracting meaningful features from MRI images.

## 3. Classification Categories

The model classifies MRI images into four categories:

- Glioma
- Meningioma
- No Tumor
- Pituitary

## 4. Accuracy Results from Optimization Experiments

The following table summarizes selected results recorded during the DenseNet-121 optimization experiments.

| Optimization Technique | Training Accuracy | Validation Accuracy | Test Accuracy |
|---|---:|---:|---:|
| Batch Normalization Experiment | 94% | 89.45% | 90% |
| Depthwise Convolution Experiment | 99.41% | 99.80% | 100% |
| Tensor Decomposition Experiment | 99.51% | 99.61% | 100% |

These values represent results from separate experiments. They should not be interpreted as results from one common training run.

## 5. Key Findings

- DenseNet-121 was selected as the best-performing CNN architecture in the study.
- Optimization techniques were investigated to understand their effects on classification accuracy and model complexity.
- Different optimization techniques produced different accuracy and parameter-count results.
- Model evaluation should consider both classification performance and computational requirements.

## 6. Conclusion

DenseNet-121 was chosen for MRI brain tumor classification because it achieved the highest classification accuracy among the CNN models evaluated in this research.

The optimization experiments further investigated ways to reduce model complexity while maintaining useful classification performance.

**Note:** The results shown above are from individual optimization experiments and are not a direct comparison of all CNN architectures.
