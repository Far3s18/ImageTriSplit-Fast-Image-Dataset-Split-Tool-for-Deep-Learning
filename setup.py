from setuptools import setup, find_packages

setup(
    name='image_trisplit',
    version='0.1.0',
    description='A fast and professional tool for splitting image datasets into train, val, and test folders.',
    author='Fares Fadi',
    author_email='faresfadi0412@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'tqdm',
        'scikit-learn'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
