from setuptools import setup, find_packages

setup(
    name="callmebot-utils",
    version="0.1.1",
    packages=find_packages(),
    install_requires=["requests"],
    author="Sakib Salim",
    author_email="salimsakib775@yahoo.com",
    description="A simple callmebot wrapper.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SAKIB-SALIM/callmebot-utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
