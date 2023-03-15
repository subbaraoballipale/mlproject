from setuptools import find_packages, setup
from typing import List
HRPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:

    '''
    This Fun will return the list from the requrimets 

    '''
    requirements= []
    with open(file_path) as  file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if HRPEN_E_DOT in requirements:
            requirements.remove( HRPEN_E_DOT)
    return requirements            

setup(
name = 'mlproject',
version ='0.0.1',
author='Subbarao ballipale',
author_email= 'subbaraoballipale@gmail.com',
packages=find_packages(),
#install_requries=['pandas','numpy','seaborn']
install_requries=get_requirements('requirements.txt')
)