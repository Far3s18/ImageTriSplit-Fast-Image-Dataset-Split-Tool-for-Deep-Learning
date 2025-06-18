# 📦 ImageTriSplit

**A blazing-fast, production-ready Python package to split image datasets into train, val, and test subsets with parallelism, logging, and smart organization.**

> Built for data scientists, ML engineers, and computer vision researchers who value speed, clarity, and maintainability.
---

## 🚀 Key Features

- ⚡ **High Performance**: Uses `ThreadPoolExecutor` to accelerate file copying using parallel threads.
- 🧠 **Smart Splitting**: Stratified splits ensure balanced label distribution across all subsets.
- 📁 **Automatic Directory Creation**: Automatically structures your dataset into the classic `train/val/test` format.
- 📊 **CSV Tracking**: Saves a `.csv` file (`split_info.csv`) detailing the location and label of each image.
- 📜 **Logging Support**: Logs every file movement and error into `split.log` for full traceability.
- ✅ **Plug-and-Play**: Easy to use, with minimal setup.

---

## 📂 Directory Structure

**Before:**

```plaintext
your_dataset/
├── class1/
│   ├── img001.jpg
│   ├── img002.jpg
│   └── ...
├── class2/
│   └── ...
└── ...
```
**After:**

```plaintext

data/processed/
├── train/
│   ├── class1/
│   ├── class2/
│   └── ...
├── val/
│   ├── class1/
│   ├── class2/
│   └── ...
├── test/
│   ├── class1/
│   ├── class2/
│   └── ...
├── split_info.csv
└── split.log
```

## 📦 Installation

```bash
pip install git+https://github.com/Far3s18/ImageTriSplit.git
```

Or install from a local copy:

```bash
cd image_trisplit
pip install .
```
## 🧑‍💻 Usage

<pre> ```python from image_trisplit import ImageTriSplitter # Example: images and labels images = ['path/to/img1.jpg', 'path/to/img2.jpg', 'path/to/img3.jpg'] labels = ['cat', 'dog', 'cat'] splitter = ImageTriSplitter(images, labels, output_dir='data/processed', log_file='split.log') splitter.split_data(test_size=0.2, valid_size=0.1) ``` </pre>

## 📈 Output

- ✅ **Images will be copied** to the `train`, `val`, and `test` folders under the specified `output_dir`.
- 🗃️ **CSV file `split_info.csv`** will be generated, containing the image paths, labels, and their assigned split group.

<pre> ```csv image,label,split /full/path/to/img1.jpg,cat,train /full/path/to/img2.jpg,dog,test /full/path/to/img3.jpg,cat,val ... ``` </pre>

- 🪵 Logs all operations and errors in split.log.

## 💡 Best Practices

- Ensure that each class has enough images for stratified splitting (at least 2–3 per class per subset).
- Avoid non-image files in your dataset directories.
- Use absolute paths when possible for robust logging.

## 🛠️ Built With

- Python
- Numpy
- Scikit-learn
- tqdm
- Threading & Logging

## 👤 Author

Fares Fadi
📧 [faresfadi0412@gmail.com](mailto:faresfadi0412@gmail.com)
