import setuptools
from dvc.testing.benchmarks.fixtures import project

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.1.0"

REPO_NAME = "CHICKEN-DISEASE-CLASSIFICATION"
AUTHOR_USER_NAME = "ankitasantape"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "ankitasantape99@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    }
)