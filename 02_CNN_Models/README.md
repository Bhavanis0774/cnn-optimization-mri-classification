# CNN Models for MRI Brain Tumor Classification

## 1. Overview

This directory contains the Convolutional Neural Network (CNN) architectures considered in the research project titled **"Study of Optimization Techniques and Their Implementation on CNN Models for Image Classification."**

The project investigates CNN models for classifying brain MRI images into four categories: Glioma, Meningioma, No Tumor, and Pituitary.

The main objectives are to evaluate classification performance, investigate model complexity, and study optimization techniques that may reduce computational requirements.

## 2. CNN Architectures

The following eight architectures are considered in this project.

| No. | Model | Description |
|---|---|---|
| 1 | DenseNet-121 | Connects layers through dense feature reuse to support effective feature extraction. |
| 2 | ResNet | Uses residual connections to facilitate the training of deep neural networks. |
| 3 | VGG16 | Uses a deep architecture built primarily from small convolutional filters. |
| 4 | MobileNetV2 | Uses an efficient architecture designed for resource-constrained devices. |
| 5 | EfficientNetB0 | Balances network depth, width, and image resolution for efficient learning. |
| 6 | SqueezeNet | Uses a compact architecture designed to reduce model size. |
| 7 | FastViT | Combines convolutional processing and attention-based techniques for efficient visual recognition. |
| 8 | ConvNeXtV2 | Uses a modernized convolutional architecture for visual recognition tasks. |

## 3. Primary Model: DenseNet-121

DenseNet-121 is the primary model used to investigate CNN optimization techniques in this project.

Its dense connectivity pattern allows feature information to be reused across multiple layers.

The model is trained using TensorFlow and Keras with the following configuration:

- Input image size: 224 × 224 pixels
- Number of classes: 4
- Batch size: 32
- Optimizer: Adam
- Initial learning rate: 0.0003
- Loss function: Sparse categorical cross-entropy
- Output activation: Softmax
- Training epochs: Up to 25
- Regularization: Batch normalization and dropout
- Training controls: Learning-rate reduction and early stopping

## 4. Optimization Techniques

The architectures are considered alongside the optimization techniques investigated in the research:

- Batch Normalization
- Weight Pruning
- Network Pruning
- Layer Pruning
- Quantization
- Depthwise Convolution
- Tensor Decomposition
- Knowledge Distillation

These techniques are studied to understand their effects on classification performance, parameter count, and model efficiency.

## 5. Evaluation Metrics

The models can be evaluated using:

- Training accuracy
- Validation accuracy
- Test accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Number of model parameters

A separate test dataset should be used for final performance reporting when available.

## 6. Directory Structure

```text
02_CNN_Models/
├── README.md
└── DenseNet121/
    ├── README.md
    └── train_densenet121.py
```



## 7. Research Objective

The objective is to identify CNN architectures and optimization techniques that provide a useful balance between classification performance and computational efficiency for MRI brain tumor classification.
