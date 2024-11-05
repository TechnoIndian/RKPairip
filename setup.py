import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="RKPairip",
	version="5.0",
	author="RK_TECHNO_INDIA",
	author_email="TechnoIndia786@gmail.com",
	description="Remove Pairip Protection with RKPairip Script & Recover String & Rebuild Apk",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Technoindian/RKPairip",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.12',
	entry_points={
		'console_scripts': [
			'RKPairip=RKPairip.RKPairip:main',
		],
	},
)
