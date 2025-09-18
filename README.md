> 🚧 **Note:** This GitHub repository is actively maintained and currently in progress. We are in the process of uploading all materials, including the dataset, source code, and benchmarking results. Please check back soon for full access.


# 🔥 Land8Fire: A Complete Study on Wildfire Segmentation through Comprehensive Review, Human-Annotated Multispectral Dataset, and Extensive Benchmarking

Land8Fire focuses on wildfire detection using high-resolution satellite imagery. Within this project, we offer Land8Fire dataset, a large-scale and high-resolution wildfire segmentation dataset designed to advance research in remote sensing-based fire detection. Alongside the dataset, this repository includes the full pipeline for preprocessing, k-fold generation, and reproducible analysis used in our study.



<!-- --- -->

## ⚙️ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/UARK-AICV/Land8Fire.git
   cd Land8Fire
   ```

2. (Optional) Create Virtual Environment
    ```
    python3 -m venv venv
    source venv/bin/activate  # or .\venv\Scripts\activate on Windows
    ```

3. Install Dependencies
    ```
    pip install -r requirements.txt
    ```


## 📦 Dataset


Our dataset has been subdivided into 5 folds, each containing images and their corresponding masks. This is the training data used in our benchmarking study. To download, run the following command:
```
python3 ./land8fire/kfolds_downloader.py
```

In addition, we provide the original full-resolution (7k × 7k) TIF images along with their manually annotated masks. You can download these using the following script:
 ```
python3 ./land8fire/downloader.py
```

The Land8Fire dataset is stored on Google Drive and organized as follows:
```
Land8Fire/
├── images/
├── masks/
└── kfolds/
    ├── kfold1/
    │   ├── images.zip
    │   └── masks.zip
    ├── kfold2/
    │   ├── images.zip
    │   └── masks.zip
    ...
    └── kfold5/
        ├── images.zip
        └── masks.zip
```


## 📁 Benchmarking
Our code is implemented on mmsegmentation and is updated rapidly. Please keep in mind you're using the same compatibility version. 

<!-- Please refer to get_started for installation and dataset_prepare for dataset preparation on mmsegmentation. -->




