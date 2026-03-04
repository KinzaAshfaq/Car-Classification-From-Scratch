# Car vs. Non-Car Binary Classification

This repository contains an end-to-end Machine Learning pipeline for binary image classification, developed as part of a technical assignment. The project focuses on data engineering, preprocessing, and the mathematical implementation of classification algorithms from scratch.

## Project Structure
- `data/`: Contains processed datasets stored in HDF5 format for efficient I/O.
- `src/`: Contains the preprocessing logic used to normalize and structure image data.
- `notebooks/`: Contains the core model implementation using NumPy.

## Data Preprocessing
The initial data pipeline involves:
1. **Normalization:** Resizing all images to a uniform $64 \times 64$ resolution.
2. **Color Space Conversion:** Standardizing images from BGR (OpenCV default) to RGB.
3. **Data Serialization:** Utilizing `h5py` to create serialized HDF5 datasets, ensuring efficient memory management during training.



## Dataset Information
- **Source:** Custom dataset of car and non-car images.
- **Format:** HDF5 (Hierarchical Data Format) used to store `train_set_x`, `train_set_y`, and test equivalents.

## Technical Details
This project demonstrates competency in:
- Matrix manipulation with NumPy.
- OpenCV for image augmentation and resizing.
- Building custom HDF5 pipelines to handle unstructured data.

---
*Developed for academic portfolio and application to the Paris-Saclay AI Master track.*
