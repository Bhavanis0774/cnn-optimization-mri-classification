# Model Parameter Comparison

## 1. Overview

This section presents the parameter-count results recorded during the optimization of DenseNet-121 for MRI brain tumor classification.

The objective is to investigate whether optimization techniques can reduce model complexity while maintaining classification performance.

## 2. Parameter Comparison

The following table summarizes the recorded parameter counts from selected experiments.

| Optimization Technique | Original Parameters | Optimized Parameters | Purpose |
|---|---:|---:|---|
| Tensor Decomposition | 6,957,956 | 5,363,188 | Reduce model parameters |
| Weight Pruning Experiment | 6,957,956 | 2,087,386 pruned parameters reported | Remove selected weights |

**Note:** The pruning experiment also recorded 4,870,570 remaining effective parameters. This value is retained as reported in the experiment and should not be interpreted as the same measurement as the pruned parameter count without checking the original implementation.

## 3. Tensor Decomposition

Tensor decomposition was investigated to reduce the number of parameters required by the model.

| Metric | Before Decomposition | After Decomposition |
|---|---:|---:|
| Training Accuracy | 99.58% | 99.51% |
| Validation Accuracy | 99.61% | 99.61% |
| Test Accuracy | 100% | 100% |
| Parameters | 6,957,956 | 5,363,188 |

The recorded parameter count decreased by 1,594,768, corresponding to an approximate reduction of 22.92%.

## 4. Weight Pruning

Weight pruning was explored as another approach to model optimization.

The recorded experiment reported:

- Original parameter count: 6,957,956
- Pruned parameter count: 2,087,386
- Remaining effective parameters: 4,870,570

Pruning can reduce the number of active weights. However, reducing the number of nonzero weights does not necessarily reduce the model file size or improve inference speed unless the implementation and hardware support the resulting sparsity.

## 5. Key Observations

- Tensor decomposition reduced the recorded parameter count while maintaining the reported test accuracy in that experiment.
- Weight pruning was investigated to reduce the number of active weights.
- Accuracy and parameter count should be considered together when evaluating an optimization technique.
- The results belong to separate experiments and should not be treated as a single controlled comparison.

## 6. Conclusion

DenseNet-121 was selected as the best-performing CNN model for MRI brain tumor classification in this research.

Parameter optimization experiments investigated ways to reduce model complexity while preserving classification performance. Further evaluation of model size, inference latency, memory usage, and hardware compatibility would help determine the practical benefits of each technique.
