import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'RasterMiner',
    version = '0.1.2.2',
    author = 'Rage Uday Kiran',
    author_email = 'uday.rage@gmail.com',
    description = 'This software is being developed at the University of Aizu, Aizu-Wakamatsu, Fukushima, Japan',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages=setuptools.find_packages(),
    url = 'https://github.com/udayRage/PAMI',
    license='GPLv3',
    install_requires=[
        'psutil',
        'pandas',
        'matplotlib',
        'resource',
        'mplcursors',
        'pandas',
        'pami',
        'sklearn-extensions',
        'tk',
        'setuptools',
        'numpy',
        'scikit-learn',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Programming Language :: Python :: 3',
	    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires = '>=3.5',
)
