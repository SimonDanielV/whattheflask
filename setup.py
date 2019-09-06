import os
from setuptools import setup, find_packages


base_packages = ["numpy>=1.15.4", "pandas>=0.23.4",
                 "Flask==1.0.3"]

dev_packages = ["pip", "pytest-cov", "pytest", "flake8"]

module_name = "wtflask"

setup(
    name=module_name,
    version="0.0.1",
    packages=find_packages(exclude=['data', 'notebooks']),
    install_requires=base_packages,
    extras_require={
        "dev": dev_packages
    }
)
