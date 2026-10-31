# ============================================================
# PROJECT: MRI BRAIN TUMOR CLASSIFICATION
# MODEL: DenseNet-121 WITH BATCH NORMALIZATION
# FRAMEWORK: TENSORFLOW / KERAS
# ============================================================

import json
import random
import time
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf

from tensorflow.keras import layers, models
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.applications.densenet import preprocess_input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import (
    ReduceLROnPlateau,
    EarlyStopping,
    ModelCheckpoint
)

from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# ============================================================
# 1. CONFIGURATION
# ============================================================

SEED = 42

random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)

# Change this path to the location of your extracted dataset.
DATASET_PATH = Path(r"C:\Users\bhava\Documents\MRI_Dataset")

TRAIN_PATH = DATASET_PATH / "Train"
VAL_PATH = DATASET_PATH / "Val"

OUTPUT_PATH = Path("outputs") / "DenseNet121_BatchNormalization"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
NUM_CLASSES = 4
EPOCHS = 25
INITIAL_LR = 0.0003

CLASS_NAMES = [
    "Glioma",
    "Meningioma",
    "No Tumor",
    "Pituitary"
]

# ============================================================
# 2. CHECK DATASET DIRECTORIES
# ============================================================

if not TRAIN_PATH.exists():
    raise FileNotFoundError(
        f"Training directory not found: {TRAIN_PATH}"
    )

if not VAL_PATH.exists():
    raise FileNotFoundError(
        f"Validation directory not found: {VAL_PATH}"
    )

print("TensorFlow version:", tf.__version__)
print("Dataset directory:", DATASET_PATH)
print("Output directory:", OUTPUT_PATH.resolve())

# ============================================================
# 3. LOAD DATASET
# ============================================================

train_ds = tf.keras.utils.image_dataset_from_directory(
    str(TRAIN_PATH),
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="int",
    shuffle=True,
    seed=SEED
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    str(VAL_PATH),
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="int",
    shuffle=False
)

class_names = train_ds.class_names

print("\nClasses detected:", class_names)

if len(class_names) != NUM_CLASSES:
    raise ValueError(
        f"Expected {NUM_CLASSES} classes, "
        f"but found {len(class_names)}: {class_names}"
    )

if train_ds.class_names != val_ds.class_names:
    raise ValueError(
        "Training and validation class directories do not match."
    )

# Save class order for future inference.
with open(OUTPUT_PATH / "class_names.json", "w") as file:
    json.dump(class_names, file, indent=4)

# ============================================================
# 4. DATA PIPELINE
# ============================================================

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

# ============================================================
# 5. DATA AUGMENTATION
# ============================================================

data_augmentation = tf.keras.Sequential(
    [
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2),
        layers.RandomZoom(0.15)
    ],
    name="data_augmentation"
)

# ============================================================
# 6. CREATE DENSENET-121 MODEL
# ============================================================

base_model = DenseNet121(
    weights="imagenet",
    include_top=False,
    input_shape=IMAGE_SIZE + (3,)
)

# Freeze the pretrained feature extractor during initial training.
base_model.trainable = False

inputs = layers.Input(
    shape=IMAGE_SIZE + (3,),
    name="input_image"
)

x = data_augmentation(inputs)

# Use DenseNet-specific preprocessing instead of Rescaling(1./255).
x = layers.Lambda(
    preprocess_input,
    name="densenet_preprocessing"
)(x)

# Keep pretrained Batch Normalization layers in inference mode.
x = base_model(x, training=False)

x = layers.GlobalAveragePooling2D(
    name="global_average_pooling"
)(x)

# Additional classification layers and Batch Normalization.
x = layers.Dense(
    512,
    activation="relu",
    name="dense_512"
)(x)

x = layers.BatchNormalization(name="batch_norm_512")(x)
x = layers.Dropout(0.5, name="dropout_512")(x)

x = layers.Dense(
    256,
    activation="relu",
    name="dense_256"
)(x)

x = layers.BatchNormalization(name="batch_norm_256")(x)
x = layers.Dropout(0.4, name="dropout_256")(x)

x = layers.Dense(
    128,
    activation="relu",
    name="dense_128"
)(x)

x = layers.BatchNormalization(name="batch_norm_128")(x)
x = layers.Dropout(0.3, name="dropout_128")(x)

outputs = layers.Dense(
    NUM_CLASSES,
    activation="softmax",
    name="classification_output"
)(x)

model = models.Model(
    inputs=inputs,
    outputs=outputs,
    name="DenseNet121_BatchNormalization"
)

# ============================================================
# 7. COMPILE MODEL
# ============================================================

model.compile(
    optimizer=Adam(learning_rate=INITIAL_LR),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# ============================================================
# 8. CALLBACKS
# ============================================================

checkpoint_path = OUTPUT_PATH / "best_densenet121.keras"

lr_scheduler = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=3,
    verbose=1
)

early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=6,
    restore_best_weights=True,
    verbose=1
)

model_checkpoint = ModelCheckpoint(
    filepath=str(checkpoint_path),
    monitor="val_loss",
    save_best_only=True,
    verbose=1
)

# ============================================================
# 9. TRAIN MODEL
# ============================================================

print("\nStarting DenseNet-121 training...")

start_time = time.perf_counter()

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS,
    callbacks=[
        lr_scheduler,
        early_stopping,
        model_checkpoint
    ],
    verbose=1
)

training_seconds = time.perf_counter() - start_time

# Restore the best model saved during training.
model = tf.keras.models.load_model(checkpoint_path)

print("\nTraining completed.")
print(f"Training duration: {training_seconds:.2f} seconds")

# ============================================================
# 10. SAVE TRAINING HISTORY
# ============================================================

history_data = {
    key: [float(value) for value in values]
    for key, values in history.history.items()
}

with open(OUTPUT_PATH / "training_history.json", "w") as file:
    json.dump(history_data, file, indent=4)

# ============================================================
# 11. PLOT ACCURACY AND LOSS
# ============================================================

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.title("DenseNet-121 Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.title("DenseNet-121 Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    OUTPUT_PATH / "training_curves.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ============================================================
# 12. EVALUATE MODEL
# ============================================================

val_loss, val_accuracy = model.evaluate(
    val_ds,
    verbose=1
)

print("\nValidation Results")
print("------------------")
print(f"Validation Loss: {val_loss:.4f}")
print(f"Validation Accuracy: {val_accuracy * 100:.2f}%")

# ============================================================
# 13. GENERATE PREDICTIONS
# ============================================================

y_true = []
y_pred = []

for images, labels in val_ds:
    predictions = model.predict(images, verbose=0)

    y_true.extend(labels.numpy().tolist())
    y_pred.extend(
        np.argmax(predictions, axis=1).tolist()
    )

# ============================================================
# 14. CLASSIFICATION METRICS
# ============================================================

accuracy = accuracy_score(y_true, y_pred)

precision = precision_score(
    y_true,
    y_pred,
    average="macro",
    zero_division=0
)

recall = recall_score(
    y_true,
    y_pred,
    average="macro",
    zero_division=0
)

f1 = f1_score(
    y_true,
    y_pred,
    average="macro",
    zero_division=0
)

print("\nClassification Metrics")
print("----------------------")
print(f"Accuracy:  {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall:    {recall * 100:.2f}%")
print(f"F1-score:  {f1 * 100:.2f}%")

report = classification_report(
    y_true,
    y_pred,
    labels=list(range(NUM_CLASSES)),
    target_names=class_names,
    output_dict=True,
    zero_division=0
)

print("\nClassification Report")
print(
    classification_report(
        y_true,
        y_pred,
        labels=list(range(NUM_CLASSES)),
        target_names=class_names,
        zero_division=0
    )
)

with open(
    OUTPUT_PATH / "classification_report.json",
    "w"
) as file:
    json.dump(report, file, indent=4)

# ============================================================
# 15. CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(
    y_true,
    y_pred,
    labels=list(range(NUM_CLASSES))
)

plt.figure(figsize=(8, 6))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=class_names,
    yticklabels=class_names
)

plt.xlabel("Predicted Class")
plt.ylabel("True Class")
plt.title("DenseNet-121 Confusion Matrix")
plt.tight_layout()

plt.savefig(
    OUTPUT_PATH / "confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ============================================================
# 16. SAVE EXPERIMENT SUMMARY
# ============================================================

summary = {
    "model": "DenseNet-121",
    "framework": "TensorFlow/Keras",
    "optimization": "Additional Batch Normalization and Dropout",
    "image_size": list(IMAGE_SIZE),
    "batch_size": BATCH_SIZE,
    "configured_epochs": EPOCHS,
    "completed_epochs": len(history.history["loss"]),
    "initial_learning_rate": INITIAL_LR,
    "best_validation_loss": float(val_loss),
    "validation_accuracy_percent": float(
        accuracy * 100
    ),
    "validation_precision_macro_percent": float(
        precision * 100
    ),
    "validation_recall_macro_percent": float(
        recall * 100
    ),
    "validation_f1_macro_percent": float(
        f1 * 100
    ),
    "training_duration_seconds": float(
        training_seconds
    ),
    "classes": class_names,
    "trainable_parameters": int(
        sum(
            np.prod(variable.shape)
            for variable in model.trainable_variables
        )
    ),
    "total_parameters": int(model.count_params())
}

with open(OUTPUT_PATH / "experiment_summary.json", "w") as file:
    json.dump(summary, file, indent=4)

# ============================================================
# 17. MODEL SUMMARY
# ============================================================

model.summary()

print("\nAll outputs saved to:")
print(OUTPUT_PATH.resolve())

print("\nGenerated files:")
print("- best_densenet121.keras")
print("- class_names.json")
print("- training_history.json")
print("- training_curves.png")
print("- confusion_matrix.png")
print("- classification_report.json")
print("- experiment_summary.json")
