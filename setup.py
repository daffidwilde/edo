""" Setup script. """

# pylint: disable=exec-used,undefined-variable

from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    README = readme_file.read()

exec(open("src/edo/version.py", "r").read())

setup(
    name="edo",
    version=__version__,
    description="Generating artificial datasets through genetic evolution.",
    long_description=README,
    url="https://github.com/daffidwilde/edo",
    author="Henry Wilde",
    author_email="henrydavidwilde@gmail.com",
    license="MIT",
    keywords=["genetic-algorithm" "data" "evolution"],
    packages=find_packages("src"),
    package_dir={"": "src"},
)
