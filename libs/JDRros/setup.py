import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jderobot-ros",
    version="1.0.2",
    author="aitormf",
    author_email="aitor.martinez.fernandez@gmail.com",
    description="ros utils package for jderobot projects",
    install_requires = ['opencv-python'],
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

