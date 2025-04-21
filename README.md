<h1 style="text-align: center;">LoRA Adapter</h1>
This repository contains a submission for NYU ECE-GY 7123 Deep Learning S25 Kaggle Competition authored by Aadit Fadia, Riya Shah and Isha Math.

## Overview
A careful tuning of mixed precision and moderate data augmentation can unlock LoRA's full potential for efficient, high accuracy text classification; with an accuracy of 90.28% under constrained parameters.

## Model Specifications
- **Model**: LoRA adapters in the last four attention layers of frozen RoBERTa-base 
- **Number of trainable parameters**: Below 1 million
- **Dataset**: AG News Dataset
- **Epochs**: 60
- **Floating Point precision format**: BF16
- **Data Augmentations**: 15 contextual augmentations
- **LoRA rank**: r =16
- **Scaling Factor**: α = 32 
- **Final Test Accuracy**: 90.28%

## Usage
1. Clone the Github Repository in your local machine terminal.
```bash
git clone https://github.com/aaf091/textClassifier-w-LoRa.git
cd textClassifier-w-LoRa/bf16
jupyter notebook      
```
or
```bash
jupyter lab
```
3. On opening jupyter, run  LORA_1_batch_size_64_data_aug (1).ipynb locally with appropriate CUDA runtime(c12-m85-a100-1 for 12 hours atleast) to reproduce training results.
- **Note**: Some notebooks may not render properly on GitHub due to metadata compatibility issues. To view them correctly, please download the notebook and open it locally using Jupyter Notebook or JupyterLab.

## Authors
- Aadit Fadia
- Riya Shah
- Isha math
