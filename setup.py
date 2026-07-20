from setuptools import find_packages,setup

from typing import List

hypenedot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

    if hypenedot in requirements:
        requirements.remove(hypenedot)

    return requirements



setup(
    name="Ml",
    version='0.0.1',
    author="burhan",
    author_email="jalalburhan615@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)