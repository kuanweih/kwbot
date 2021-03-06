import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kwbot",
    version="0.0.1",
    author="Kuan-Wei Huang",
    author_email="kuanweih@andrew.cmu.edu",
    description="Some useful functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kuanweih/kwbot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
