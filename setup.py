from setuptools import find_packages,setup
from typing import List

Hype_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
   '''
This function will return the list of requirements 
   '''
   requirements=[]
   with open(file_path) as file_obj:
      requirements=file_obj.readlines()
      requirements=[req.replace("\n","") for req in requirements]


      if Hype_e_dot in requirements:
         requirements.remove(Hype_e_dot)
         
   return requirements




setup(
name='mlproject',
version='0.0.1',
author='Ayush',
author_email='ayushpandey24aug@gmail.com',
packages=find_packages(),

install_requires=get_requirements('requirements.txt')




)