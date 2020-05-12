from setuptools import setup, find_packages

setup(
    name='pan_xinhuan',
    version='1.0',
    packages=find_packages(),
    entry_points={
    'console_scripts': [
        'mysoftware=pan.main:main',
    ]
    },   
    install_requires=[
        'numpy',
        'vaderSentiment',
        'torch',
        'spacy',
          
    ]
)