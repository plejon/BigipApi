from setuptools import setup

setup(
    name="BigipApi",
    author="per lejon",
    author_email="per@lejon.org",
    url="https://github.com/plejon/BigipApi",
    version="1.0",
    packages=["BigipApi"],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    long_description=open("README.md").read(),
    install_requires=["setuptools>=38.4.0", "requests>=2.23.0"],
)