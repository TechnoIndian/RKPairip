import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rkjp",
    version="2.0.0",
    author="RK_TECHNO_INDIA",
    author_email="TechnoIndia555@gmail.com",
    description="Recover String & Rebuild Apk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/Technoindian/RKPairip",
    keywords='RKPairip',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            'RKPairip=RKPairip.__main__:RK_Techno_IND',
        ],
    },
)
