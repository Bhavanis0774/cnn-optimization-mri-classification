# Tensor Decomposition in CNN Models

## 1. Introduction

Tensor decomposition is a model optimization technique that represents large weight tensors using smaller components.

In CNNs, it can reduce the number of parameters and computational requirements while attempting to preserve classification performance.

This project investigates tensor decomposition for MRI brain tumor classification using DenseNet-121.

## 2. Objectives

- Reduce the number of model parameters.
- Investigate the effect on classification accuracy.
- Explore reductions in model complexity.
- Evaluate the trade-off between accuracy and efficiency.

## 3. Methodology

The experiment involves:

1. Training or loading the baseline DenseNet-121 model.
2. Identifying suitable weight tensors for decomposition.
3. Applying an appropriate tensor decomposition method.
4. Constructing the modified model.
5. Evaluating the modified model using the same evaluation procedure.
6. Comparing accuracy and parameter counts.

## 4. Recorded Experimental Results

The following results were recorded for the tensor decomposition experiment.

| Metric | Before Decomposition | After Decomposition |
|---|---:|---:|
| Training Accuracy | 99.58% | 99.51% |
| Validation Accuracy | 99.61% | 99.61% |
| Test Accuracy | 100% | 100% |
| Model Parameters | 6,957,956 | 5,363,188 |

## 5. Parameter Reduction

| Measurement | Value |
|---|---:|
| Original Parameters | 6,957,956 |
| Parameters After Decomposition | 5,363,188 |
| Parameters Reduced | 1,594,768 |
| Percentage Reduction | Approximately 22.92% |

The reported experiment reduced the parameter count by approximately **22.92%** while maintaining the reported validation and test accuracy.

## 6. Results Analysis

The recorded training accuracy decreased slightly from 99.58% to 99.51%. Validation accuracy remained at 99.61%, and test accuracy remained at 100%.

These results indicate that the reported decomposition experiment reduced the parameter count while maintaining the reported validation and test performance.

## 7. Advantages

Tensor decomposition can provide:

- Reduced parameter count
- Potentially lower storage requirements
- Reduced computational complexity
- Opportunities for efficient model deployment

The actual benefits depend on the decomposition method and implementation.

## 8. Conclusion

Tensor decomposition is a promising approach for reducing CNN model complexity. In the recorded DenseNet-121 experiment, the parameter count decreased by approximately 22.92% while the reported test accuracy remained unchanged.
