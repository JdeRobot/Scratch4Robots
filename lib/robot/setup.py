import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robot-scratch4robots",
    version="1.0.7",
    author="carrionvs",
    author_email="carrionvs@gmail.com",
    description="robot lib for scratch4robots projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JdeRobot/Scratch4Robots",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

