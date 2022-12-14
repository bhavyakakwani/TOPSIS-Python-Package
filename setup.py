from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name = "Topsis_Bhavya_101903365",
    version = "1.0.1",
    description = "A Python package implementing TOPSIS technique.",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    author = "Bhavya Kakwani",
    author_email = "bhavyakakwani@gmail.com",
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["Topsis_Bhavya_101903365"],
    include_package_data = True,
    install_requires = ["pandas"],
)