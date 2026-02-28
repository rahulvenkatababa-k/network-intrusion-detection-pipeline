'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() ->List[str]:

    # this function will return list of requirements
    requirements_list:List[str] = []

    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found")
    return requirements_list

setup(
    name="NetworkSecurity",
    version='0.0.1',
    author="Rahul Venkata Baba, Kalidindi",
    packages=find_packages(),
    author_email="rahulvenkatababa@gmail.com",
    install_requires=get_requirements()
)