import os
import shutil
from multiprocessing import cpu_count
from pathlib import Path
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import pandas as pd

from .utils import setup_logger, make_dirs


class ImageTriSplitter:
    def __init__(self, images, labels, output_dir='data/processed', log_file='split.log'):
        self._images = np.array(images)
        self._labels = np.array(labels)
        self.output_dir = Path(output_dir).resolve()
        self.logger = setup_logger(log_file)

    def _copy_file(self, src_label_tuple, dest_root):
        try:
            src, label = src_label_tuple
            class_dir = dest_root / str(label)
            class_dir.mkdir(parents=True, exist_ok=True)

            dest_path = class_dir / Path(src).name
            shutil.copy2(src, dest_path)
            self.logger.info(f"Copied: {src} -> {dest_path}")
        except Exception as e:
            self.logger.error(f"Failed to copy {src}: {e}")

    def _copy_files(self, file_paths, labels, destination):
        make_dirs(destination)
        with ThreadPoolExecutor(max_workers=min(32, cpu_count() + 4)) as executor:
            src_label_pairs = list(zip(file_paths, labels))
            list(tqdm(executor.map(lambda item: self._copy_file(item, destination), src_label_pairs),
                      total=len(file_paths), desc=f'Copying to {destination.name}'))

    def split_data(self, test_size, valid_size):
        self.logger.info("Starting dataset split...")

        os.makedirs(self.output_dir, exist_ok=True)

        x_train, x_test, y_train, y_test = train_test_split(
            self._images, self._labels, test_size=test_size, random_state=42, stratify=self._labels
        )

        val_ratio = valid_size / (1 - test_size)
        x_train, x_val, y_train, y_val = train_test_split(
            x_train, y_train, test_size=val_ratio, random_state=42, stratify=y_train
        )

        train_folder = self.output_dir / 'train'
        val_folder = self.output_dir / 'val'
        test_folder = self.output_dir / 'test'

        self._copy_files(x_train, y_train, train_folder)
        self._copy_files(x_val, y_val, val_folder)
        self._copy_files(x_test, y_test, test_folder)

        df = pd.DataFrame({
            'image': np.concatenate([x_train, x_val, x_test]),
            'label': np.concatenate([y_train, y_val, y_test]),
            'split': ['train'] * len(x_train) + ['val'] * len(x_val) + ['test'] * len(x_test)
        })
        df.to_csv(self.output_dir / 'split_info.csv', index=False)

        self.logger.info("Data split and copy completed..")
        print("Data split and copy completed..")
