# setup.py

from setuptools import setup, find_packages

setup(
    name='easy_argparse',
    version='0.1.0',
    author='Stefano Di Paola',
    author_email='steve.wisec@gmail.com',
    description='A utility to simplify the creation of argparse parsers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wisec/easy_argparse',  # Optional
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)