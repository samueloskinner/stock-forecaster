from setuptools import setup, find_packages

setup(
    name='stockforecaster',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A library to read the latest stock price of Microsoft and forecast it for the next 30 days.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas>=1.5.0',
        'numpy>=1.21.0',
        'matplotlib>=3.5.0',
        'yfinance>=0.2.0',
        'prophet>=1.1.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)