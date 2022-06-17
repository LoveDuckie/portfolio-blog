from typing import List
import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
def get_requirements_filepath() -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "requirements.txt")

def get_requirements() -> List:
    requirements = []
    with open(get_requirements_filepath(), 'r') as f:
        requirements = f.readlines()
    return requirements

requirements_found = get_requirements()

def get_project_url(*args) -> str:
    parts = os.sep.join(args)
    return f'https://github.com/LoveDuckie/portfolio-blog/{parts}'

setuptools.setup(
    name="publisher",
    version="0.0.1",
    author="Luc Shelton",
    author_email="lucshelton@gmail.com",
    description="A Python application responsible for processing and publishing markdown blogs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=get_project_url("/tree/main/scripts/python/publisher"),
    project_urls={
        "Bug Tracker": get_project_url("issues"),
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=requirements_found,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)