import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyhustler-ashdaily",
    version="0.3.0",
    author="Ashish Singh Bardhan",
    author_email="ashtokyo31@gmail.com",
    description="Useful tools for daily python/django hustles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashdaily/pyhustler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)