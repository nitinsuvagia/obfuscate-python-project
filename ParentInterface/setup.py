from setuptools import setup, find_packages

setup(
    name="obfuscate-python",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,  # Include all data files (important for including pytransform)
    package_data={
        "my_interface": ["pytransform/*"],  # Include all files in the pytransform directory
    },
    install_requires=[],
    description="An obfuscated Python package containing ParentInterface",
    author="Nitin Suvagiya",
    author_email="nitin@softqubes.com",
    url="https://github.com/nitinsuvagia/obfuscate-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
