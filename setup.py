import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-lastfm",
    version="1.0.0",
    author="mytja",
    license='MIT',
    author_email="mytja@protonmail.com",
    description="Get charts, top artists and top songs WITHOUT LastFM API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mytja/lastfm-py",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'httpx'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
