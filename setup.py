from setuptools import setup, find_packages

setup(
    name="bank-transactions-analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.22.0",
        "pandas==1.3.5",
        "matplotlib==3.4.3",
        "seaborn==0.11.2",
        "numpy==1.21.6",
        "pillow==9.0.1",
        "python-dateutil==2.8.2",
        "protobuf==3.20.0",
        "typing-extensions==4.3.0"
    ],
    python_requires=">=3.9",
) 