import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jderobot-jderobottypes",
    version="1.0.0",
    author="aitormf",
    author_email="aitor.martinez.fernandez@gmail.com",
    description="package of types for jderobot project",
    install_requires = ['numpy'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JdeRobot/JdeRobot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

