"""
Setuptools based setup module
"""
from setuptools import setup, find_packages

setup(
    name='pytables_blosc2_and_pipcheck',
    version='0',
    description='MWE for pytables downstream pip check issues',
    author_email='liamhuber@greyhavensolutions.com',
    license='BSD',

    classifiers=[
                 'Programming Language :: Python :: 3.11'
                ],

    keywords='',
    packages=find_packages(exclude=["*.github*", "*.ci_support*"]),
    install_requires=[
        'tables==3.9.2',
    ],
)
