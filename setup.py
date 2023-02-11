from setuptools import setup, find_packages

setup(
    name='example_library',
    version='0.1.0',
    author='John Doe',
    author_email='johndoe@example.com',
    description='Audio Description Tools',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'tkinter',
    ],
)
