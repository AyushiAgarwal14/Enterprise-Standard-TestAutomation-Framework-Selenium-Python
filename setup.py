from collections import defaultdict

import setuptools

# project_name = input("Enter the project name: ")
setuptools.setup(
    name="Shell-FE-Selenium-Core",
    version='2.0.2',
    author="Sakthivel Rajasekar",
    author_email="sakthivel.rajasekar@shell.com",
    description="Selenium Core package to be used along with the Shell FE Behave framework for Web application "
                "automation.",
    long_description_content_type='text/markdown',
    license="Proprietary",
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent'
    ],
    packages=setuptools.find_packages(exclude=["Shell_FE_Behave_Tests"]),
    python_requires='>=3.9',
    install_requires=[],

)
