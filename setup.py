import setuptools


setuptools.setup(
    name="calcapp",
    version="0.1",
    author="Deepan",
    author_email="deepan0433@gmail.com",
    description="A CLI tool for calc",
    long_description="A CLI tool for calc",
    long_description_content_type="text/markdown",
    url="https://github.com/deepan10/jxctl",
    packages=setuptools.find_packages(exclude=["tests"]),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'calcapp = src.calcapp:start'
        ]
    },
)