# MRI Brain Tumor Classification Dataset

## 1. Dataset Overview

This project uses a Magnetic Resonance Imaging (MRI) brain image dataset to study Convolutional Neural Networks (CNNs) and optimization techniques for brain tumor classification.

The objective is to classify MRI images into four categories and investigate methods to improve model performance, reduce model complexity, and support deployment in resource-constrained environments.

## 2. Dataset Classes

The dataset contains four classes:

| Class | Description |
|---|---|
| Glioma | MRI images associated with glioma tumors |
| Meningioma | MRI images associated with meningioma tumors |
| No Tumor | MRI images without a detected brain tumor |
| Pituitary | MRI images associated with pituitary tumors |

## 3. Image Specifications

| Property | Value |
|---|---|
| Image type | Brain MRI |
| Number of classes | 4 |
| Input image size | 224 × 224 pixels |
| Model input format | RGB images |
| Training framework | TensorFlow and Keras |
| Primary CNN model | DenseNet-121 |

## 4. Dataset Organization

The dataset is expected to contain separate training and validation folders, with one subfolder for each class.

```text
MRI_Dataset/
├── Train/
│   ├── Glioma/
│   ├── Meningioma/
│   ├── No Tumor/
│   └── Pituitary/
└── Val/
    ├── Glioma/
    ├── Meningioma/
    ├── No Tumor/
    └── Pituitary/
```

Each class folder should contain the corresponding MRI images.

**Important:** The directory structure above must match the structure expected by the training script. If your dataset contains additional folders, such as `images` and `labels`, the data-loading code may need to be adapted.

## 5. Dataset Preprocessing

The training pipeline uses the following preprocessing operations:

1. Load MRI images from the training and validation directories.
2. Resize images to 224 × 224 pixels.
3. Assign class labels based on directory names.
4. Apply data augmentation to training images using random horizontal flipping, rotation, and zooming.
5. Apply the preprocessing expected by the pretrained DenseNet-121 model.
6. Prepare image batches for training and validation.

## 6. Dataset Splitting

The training and validation sets are maintained in separate directories.

- **Training set:** Used to train the CNN model.
- **Validation set:** Used to monitor model performance, adjust the learning rate, and apply early stopping.

A separate test set should be used for final evaluation if available. Validation accuracy should not be reported as test accuracy.

## 7. Role in the Research

The dataset is used to evaluate the baseline DenseNet-121 model and study the effects of optimization techniques, including:

- Batch normalization
- Weight pruning
- Network pruning
- Layer pruning
- Quantization
- Depthwise convolution
- Tensor decomposition
- Knowledge distillation

The experiments investigate classification performance alongside model complexity and parameter reduction.

## 8. Reproducibility

For reproducible experiments, record the dataset source, class-wise image counts, training and validation split, random seed, preprocessing settings, and software versions.

The exact image counts and dataset source should be documented after verifying the dataset used for the experiments.
