""" Setup script. """

from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    README = readme_file.read()

setup(
    name="genetic_data",
    version="0.0.1",
    description="A library for generating artificial datasets through genetic \
    evolution.",
    long_description=README,
    url="https://github.com/daffidwilde/genetic_data",
    author="Henry Wilde",
    author_email="henrydavidwilde@gmail.com",
    license="MIT",
    keywords=["genetic-algorithm" "data" "evolution"],
    packages=find_packages("src"),
    package_dir={"": "src"},
)
