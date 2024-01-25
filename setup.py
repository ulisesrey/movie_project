from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='programming for data science PAC4',
    version='1.0.0',
    author='Ulises Rey',
    author_email='ulises.rey.torne@gmail.com',
    description='A short description of your package',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package requires
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
