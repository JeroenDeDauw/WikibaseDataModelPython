from setuptools import setup, find_packages

setup(
    name='WikibaseDataModel',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/JeroenDeDauw/WikibaseDataModelPython',
    license='GPL v2+',
    author='Jeroen De Dauw',
    author_email='jeroendedauw@gmail.com',
    description='Implementation of the Wikibase DataModel in Python',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)'
    ],
    include_package_data=True,
    install_requires=[
        "unittest-data-provider >= 1.0.1"
    ]
)
