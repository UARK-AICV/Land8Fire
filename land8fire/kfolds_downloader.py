"""
Download and extract the **Land8Fire K-Folds dataset** from Google Drive.

Requirements:
    pip install gdown

"""

import os
import gdown
import zipfile

base_url = 'https://drive.google.com/uc?id={}'
output_directory = "./dataset"
dataset_name = "kfolds"
kfolds_file = f"{output_directory}/{dataset_name}.zip"

datasets = {
    "kfolds": "1g3IH83bNcLtfJTrrjShNzvnHbTYXywt",
}

if not os.path.exists(output_directory):
    os.makedirs(output_directory, exist_ok=True)

print("Downloading Land8Fire Kfolds Datasets")
kfolds_dataset_url = base_url.format(datasets[dataset_name])
kfolds_download = gdown.download(kfolds_dataset_url, f"{dataset_name}.zip")

if kfolds_download:

    print("Extracting Land8Fire Kfolds Dataset")
    with zipfile.ZipFile(kfolds_file, 'r') as zip_ref:
        zip_ref.extractall(output_directory)

    folds = os.listdir(os.path.join(output_directory, dataset_name))
    for fold in folds:
        fold_directory = os.path.join(output_directory, dataset_name, fold)
        files = os.listdir(fold_directory)
        for file in files:
            with zipfile.ZipFile(os.path.join(fold_directory, file), 'r') as zip_ref:
                zip_ref.extractall(fold_directory)

else:
    print('"Skipping extraction: Land8Fire Kfold Datasets was not downloaded successfully."')

