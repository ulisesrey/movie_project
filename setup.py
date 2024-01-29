from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='movie_project',
    version='1.0.0',
    author='Ulises Rey',
    author_email='ulises.rey.torne@gmail.com',
    description='A package to analyze the TMDB dataset',
    packages=find_packages(),
    # List any dependencies your package requires
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
