# Quantization in CNN Models

## 1. Introduction

Quantization is a deep learning optimization technique that represents model weights and activations using lower-precision numerical formats.

This project investigates quantization as a method for reducing the memory requirements and computational cost of CNN models used for MRI brain tumor classification.

## 2. Objectives

- Reduce model storage requirements.
- Investigate the effect of quantization on classification accuracy.
- Explore efficient model deployment.
- Compare model performance before and after quantization.

## 3. Methodology

The quantization workflow consists of the following steps:

1. Train or load the baseline CNN model.
2. Select an appropriate quantization method.
3. Convert model weights or operations to the selected numerical precision.
4. Evaluate the quantized model.
5. Compare accuracy, model size, and inference performance with the baseline.

## 4. Types of Quantization

### 4.1 Post-Training Quantization

Post-training quantization converts a trained model to a lower-precision representation without requiring a complete retraining process.

### 4.2 Quantization-Aware Training

Quantization-aware training simulates quantization effects during training to help the model adapt to lower-precision computation.

## 5. Recorded Experimental Result

One reported experiment using ClipQ quantization recorded the following test accuracies:

| Measurement | Test Accuracy |
|---|---:|
| Before Quantization | 99.61% |
| After Quantization | 94.34% |

The recorded result shows a decrease of **5.27 percentage points** in test accuracy after quantization.

## 6. Evaluation Metrics

Quantization can be evaluated using:

- Test accuracy
- Precision, recall, and F1-score
- Model size
- Numerical precision
- Inference latency
- Memory requirements

## 7. Advantages

Quantization may provide:

- Reduced model storage
- Lower memory usage
- Faster inference on compatible hardware
- Lower computational requirements

The benefits depend on the quantization method, model architecture, and deployment hardware.

## 8. Conclusion

Quantization can improve CNN deployment efficiency, but reduced numerical precision may affect classification accuracy. The optimal configuration should balance model efficiency and reliable MRI brain tumor classification.
