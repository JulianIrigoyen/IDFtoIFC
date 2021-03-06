import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='idf-to-ifc',  # should match the package folder
    packages=['idf-to-ifc'],  # should match the package folder
    version='0.0.1',  # important for updates
    license='MIT',  # should match your chosen license
    description='Codebase to transform IDF files to IFC format. ',
    long_description=long_description,  # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='Ángel Díaz Murillo',
    author_email='angel_diaz_murillo@hotmail.com',
    url='https://github.com/mike-huls/toolbox_public',
    install_requires=[''],  # list all packages that your package uses
    keywords=["pypi", "idf-to-ifc"],
    classifiers=[  # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    download_url="https://github.com/JulianIrigoyen/IDFtoIFC/archive/refs/tags/0.0.1.tar.gz",
)