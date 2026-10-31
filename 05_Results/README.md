# Results and Performance Analysis

## 1. Overview

This section presents the recorded experimental results from the research project, **"Study of Optimization Techniques and Their Implementation on CNN Models for Image Classification."**

The project investigates CNN optimization techniques for MRI brain tumor classification using four classes:

- Glioma
- Meningioma
- No Tumor
- Pituitary

The evaluation focuses on classification accuracy and model parameter reduction.

## 2. Batch Normalization Results

The following results were recorded for DenseNet-121.

| Metric | Without Optimization | With Batch Normalization |
|---|---:|---:|
| Training Accuracy | 90% | 94% |
| Validation Accuracy | 88% | 89.45% |
| Test Accuracy | 88% | 90% |
| Model Parameters | 7,432,654 | Not specified |

### Analysis

The recorded results show improvements in training, validation, and test accuracy after optimization.

## 3. Depthwise Convolution Results

| Metric | Original Model | Depthwise Convolution |
|---|---:|---:|
| Training Accuracy | 99.32% | 99.41% |
| Validation Accuracy | 99.22% | 99.80% |
| Test Accuracy | 99% | 100% |
| Model Parameters | 6,957,956 | 7,050,000 |

### Analysis

The recorded classification accuracy improved in this experiment. However, the reported parameter count increased, so this result does not demonstrate parameter reduction.

## 4. Tensor Decomposition Results

| Metric | Before Decomposition | After Decomposition |
|---|---:|---:|
| Training Accuracy | 99.58% | 99.51% |
| Validation Accuracy | 99.61% | 99.61% |
| Test Accuracy | 100% | 100% |
| Model Parameters | 6,957,956 | 5,363,188 |

### Parameter Reduction

| Measurement | Value |
|---|---:|
| Original Parameters | 6,957,956 |
| Parameters After Decomposition | 5,363,188 |
| Parameters Reduced | 1,594,768 |
| Percentage Reduction | Approximately 22.92% |

### Analysis

The recorded parameter count decreased by approximately 22.92%, while the reported validation and test accuracy remained unchanged.

## 5. Pruning Results

| Metric | Recorded Value |
|---|---:|
| Training Accuracy Before Pruning | 99.66% |
| Validation Accuracy Before Pruning | 99.41% |
| Test Accuracy Before Pruning | 99% |
| Original Model Parameters | 6,957,956 |
| Pruned Parameters | 2,087,386 |
| Remaining Effective Parameters | 4,870,570 |

### Analysis

The recorded experiment identifies 2,087,386 pruned parameters and 4,870,570 remaining effective parameters.

Actual reductions in storage and inference time depend on how the sparse model is represented and deployed.

## 6. Quantization Results

One reported ClipQ quantization experiment recorded the following test accuracy.

| Measurement | Test Accuracy |
|---|---:|
| Before Quantization | 99.61% |
| After Quantization | 94.34% |
| Difference | -5.27 percentage points |

### Analysis

The reported experiment shows a decrease of 5.27 percentage points in test accuracy after quantization. This illustrates the trade-off that can occur between numerical precision and classification performance.

## 7. Performance Comparison Summary

| Optimization Technique | Main Observation |
|---|---|
| Batch Normalization | Improved reported training, validation, and test accuracy |
| Depthwise Convolution | Improved reported accuracy, but parameter count increased |
| Tensor Decomposition | Reduced reported parameter count by approximately 22.92% |
| Weight Pruning | Reduced the number of active weights in the recorded experiment |
| Quantization | Reduced reported test accuracy in the ClipQ experiment |
| Network Pruning | Investigated as a method to reduce model complexity |
| Layer Pruning | Investigated as a method to reduce network depth |
| Knowledge Distillation | Investigated as a method to transfer knowledge to a smaller model |

## 8. Conclusion

The recorded results show that optimization techniques can have different effects on classification performance and model complexity.

Tensor decomposition reduced the reported parameter count while maintaining the recorded validation and test accuracy. Quantization reduced the reported test accuracy, while the depthwise convolution experiment showed improved accuracy but a higher parameter count.

These findings demonstrate the importance of evaluating both classification performance and model efficiency when selecting optimization techniques for MRI brain tumor classification.
