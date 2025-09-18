"""
Download and extract the **original full-sized (7k × 7k resolution) Land8Fire dataset** from Google Drive.

Requirements:
    pip install gdown

"""

import os
import gdown
import zipfile

base_url = 'https://drive.google.com/uc?id={}'
output_directory = "./dataset"
image_file = f"{output_directory}/images.zip"
mask_file = f"{output_directory}/masks.zip"

datasets = {
    "images": "1PrT2HI_bbo1tkGhGqZDEpp9IUiW_GxNX",
    "masks": "1VwKo1q_JTKldmIUP4_ybdQyqeMk37iUk"
}

if __name__=="__main__":

    if not os.path.exists(output_directory):
        os.makedirs(output_directory, exist_ok=True)

    print("Downloading Land8Fire Images Dataset") 
    images_dataset_url = base_url.format(datasets["images"])
    images_download = gdown.download(images_dataset_url, image_file)

    if images_download:
        print("Extracting Land8Fire Images Dataset")
        with zipfile.ZipFile(image_file, 'r') as zip_ref:
            zip_ref.extractall(output_directory)
    else:
        print('"Skipping extraction: Land8Fire Images was not downloaded successfully."')


    print("Downloading Land8Fire Masks Dataset")
    masks_dataset_url = base_url.format(datasets["masks"])
    masks_download = gdown.download(masks_dataset_url, mask_file)

    if masks_download:
        print("Extracting Land8Fire Masks Dataset")
        with zipfile.ZipFile(mask_file, 'r') as zip_ref:
            zip_ref.extractall(output_directory)
    else:
        print('"Skipping extraction: Land8Fire Masks was not downloaded successfully."')

