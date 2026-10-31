# Weight Pruning in CNN Models

## 1. Introduction

Weight pruning is a neural network optimization technique that removes or sets selected weights to zero to produce a sparse model.

In this project, weight pruning is studied as a method to reduce model complexity while maintaining classification performance for MRI brain tumor classification.

## 2. Objectives

- Reduce the number of significant model weights.
- Investigate the effect of pruning on classification accuracy.
- Compare model complexity before and after pruning.
- Explore potential reductions in memory and computational requirements.

## 3. Methodology

The pruning process involves:

1. Training the original CNN model.
2. Identifying weights selected by the pruning strategy.
3. Setting selected weights to zero.
4. Evaluating the pruned model.
5. Comparing model performance and parameter counts.

## 4. Recorded DenseNet-121 Results

The following results were recorded for a pruning-related experiment.

| Metric | Recorded Value |
|---|---:|
| Training Accuracy Before Pruning | 99.66% |
| Validation Accuracy Before Pruning | 99.41% |
| Test Accuracy Before Pruning | 99% |
| Original Model Parameters | 6,957,956 |
| Pruned Parameters | 2,087,386 |
| Remaining Effective Parameters | 4,870,570 |

## 5. Results Analysis

The recorded experiment identifies 2,087,386 pruned parameters and 4,870,570 remaining effective parameters.

Pruning can create sparse models, but setting weights to zero does not automatically reduce the stored model size or inference time. Actual savings depend on the implementation, hardware, and support for sparse computation.

## 6. Evaluation Metrics

The pruning experiment can be evaluated using:

- Training accuracy
- Validation accuracy
- Test accuracy
- Number of pruned parameters
- Remaining effective parameters
- Model storage size
- Inference latency

## 7. Conclusion

Weight pruning can reduce the number of active weights in a CNN. Its practical benefits depend on the pruning strategy and whether the target hardware and deployment framework efficiently support sparse models.
