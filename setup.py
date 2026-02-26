from setuptools import  find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='ML_pipeline_project',
    version='0.0.1',
    description='ML pipeline project for end to end ML project',
    author='Farah',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
    )