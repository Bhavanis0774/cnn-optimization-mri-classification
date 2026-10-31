# Layer Pruning in CNN Models

## 1. Introduction

Layer pruning is a neural network optimization technique that removes selected layers from a model to reduce its depth and computational complexity.

This project investigates CNN optimization techniques for MRI brain tumor classification, with DenseNet-121 serving as the primary model.

## 2. Objectives

- Investigate the effect of removing selected network layers.
- Reduce model depth and computational requirements.
- Evaluate the effect on classification accuracy.
- Explore opportunities to make CNN models more efficient.

## 3. Methodology

The layer pruning workflow consists of the following steps:

1. Train the original CNN model.
2. Identify layers that may be suitable for removal.
3. Construct a modified model without the selected layers.
4. Train or fine-tune the modified model as required.
5. Evaluate its classification performance.
6. Compare the modified model with the original model.

## 4. Application to DenseNet-121

DenseNet-121 contains densely connected convolutional layers that support feature reuse.

Removing layers from this architecture requires careful consideration of its connectivity structure. The modified network must maintain compatible tensor dimensions and valid connections.

## 5. Evaluation Metrics

The following metrics can be used to evaluate layer pruning:

- Training accuracy
- Validation accuracy
- Test accuracy
- Precision
- Recall
- F1-score
- Total number of parameters
- Model size
- Inference latency

## 6. Advantages

Layer pruning may reduce:

- Network depth
- Computational operations
- Memory requirements
- Inference time

The actual improvements depend on the layers removed and the target hardware.

## 7. Conclusion

Layer pruning provides a possible approach to reducing CNN complexity. Its effectiveness must be evaluated by comparing the original and modified models using consistent experimental settings.
