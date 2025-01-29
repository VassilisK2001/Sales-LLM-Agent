from setuptools import setup, find_packages
from pathlib import Path

# Read the requirements from the requirements.txt file
requirements = Path('requirements.txt').read_text().splitlines()

setup(
    name="meeting-ai-agent",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,  # Automatically include dependencies
)