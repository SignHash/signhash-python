import setuptools


setuptools.setup(
    name="signhash",
    version="0.1.0",
    url="https://github.com/SignHash/signhash-cli",

    author="SignHash",

    description="SignHash for Python",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[

    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
