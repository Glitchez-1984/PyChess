from setuptools import setup, find_packages

setup(
    name="PyBoard",
    version="0.1",
    author="David",
    description="module for a chess set and board",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pygame"
    ]
)