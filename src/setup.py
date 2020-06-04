import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='v13r93w1nn7',
    version='0.0.6',
    author='Patrick Bucher',
    author_email='patrick.bucher@mailbox.org',
    description='extended version of the board game «Vier gewinnt»',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/patrickbucher/v13r93w1nn7',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
