import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drone-scratch4robots",
    version="1.0.3",
    author="carrionvs",
    author_email="carrionvs@gmail.com",
    description="drone lib for scratch4robots projects",
    install_requires = ['imutils'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JdeRobot/Scratch4Robots",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

