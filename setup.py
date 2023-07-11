from setuptools import setup, find_packages

setup(
    name='ron-bot',
    version='0.1',
    packages=find_packages(),
    description='A brief description of your package',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/your-package-name',
    install_requires=[
        'numpy',  # for example, if your package requires numpy
        'chess',  # and python-chess
    ],
)
