from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
parent_directory = path.dirname(this_directory)
with open(path.join(parent_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'PyShare',         # How you named your package folder (MyLib)
  packages = ['pyshare'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  license='Apache License 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This a repository that provides a Pythonic interface to interact with Microsoft Sharepoint',   # Give a short description about your library
  author = 'Debabrata Roy Chowdhury',                   # Type in your name
  author_email = 'debabrata.rc@dexterai.com',      # Type in your E-Mail
  url = 'https://github.com/dexterai-lab/PyShare',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/dexterai-lab/quantumdl/archive/v0.1-alpha.tar.gz',    # I explain this later on
  keywords = ['SHAREPOINT', 'PYTHON', 'MICROSOFT SHAREPOINT'],   # Keywords that define your package best
  python_requires=('>=3.6.0'),
  install_requires=[            # I get to this in a second
          'shareplum'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'   # Again, pick a license
  ],
)