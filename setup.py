from setuptools import setup

# # read the contents of your README file
# from os import path
# this_directory = path.abspath(path.dirname(__file__))
# parent_directory = path.dirname(this_directory)
# with open(path.join(parent_directory, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name='pysharepoint',
    packages=['pysharepoint'],
    version='0.1.1',
    license='GNU General Public License v3 (GPLv3)',
    description='This a repository that provides a Pythonic interface to interact with Microsoft Sharepoint',
    author='Debabrata Roy Chowdhury',
    author_email='debabrata.rc@dexterai.com',
    url='https://github.com/dexterai-lab/PyShare',
    download_url='https://github.com/dexterai-lab/PyShare/archive/0.1.1.tar.gz',
    keywords=['SHAREPOINT', 'PYTHON', 'MICROSOFT SHAREPOINT'],
    python_requires=('>=3.6.0'),
    install_requires=[
        'shareplum'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
)