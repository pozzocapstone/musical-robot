# SET UP FILE:
# in order to run in notebooks as an import musicalrobot
# 1. Git clone the repository to a local computer
# 2. go to the outermost musical-robot folder
# 3. use "pip install . "
# 4. import packages into a jupyter notebook using "from musicalrobot import xxxxxx"

import setuptools

setuptools.setup(name='musicalrobot',
    version='0.978',
    url = 'https://github.com/pozzocapstone/musical-robot',
    license = 'MIT',
    author = 'Shrilakshmi Bonageri, Jaime Rodriguez, Sage Scheiwiller',
    description= 'A package for high-throughput measurement of deep eutectic solvents’ melting point using IR bolometry',
    description_content_type = 'text/markdown; charset=UTF-8; variant=GFM',
    short_description = 'Melting temperature determination using IR bolometry',
    short_description_content_type = 'text/markdown',
    long_description = open('README.md','r').read(),
    long_description_content_type = 'text/markdown; charset=UTF-8; variant=GFM',
    packages = setuptools.find_packages(),
    install_requires = ['numpy',
                        'pandas',
                        'scikit-image',
                        'scikit-learn',
                        'scipy',
                        'matplotlib',
                        'h5py'],
    zip_safe = False,
)
