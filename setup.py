from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()
    setup(
        name="pybible-cli",
        version="1.2.5",
        description="Bible reference CLI application",
        long_description_content_type="text/markdown",
        long_description=README,
        url="https://github.com/vitorpio/pybible-cli",
        author="Vitor Pio",
        author_email="vitormarquespio@gmail.com",
        license="MIT License",
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        install_requires=["importlib_resources;python_version<'3.7'",
                          'jsonpickle'],
        packages=find_packages(exclude=("tests",)),
        include_package_data=True,
        entry_points={"console_scripts": ["pybible=pybible.__main__:main"]}
    )
