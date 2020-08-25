from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='maccorcyclingdata',
    version='0.0.1',
    description='Python Package for Publicationto perform basic functions on Maccor Battery Cycling Data',
    long_description_content_type="text/x-rst",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Shriya Challam',
    author_email='shriyachallam10@gmail.com',
    keywords=['Battery', 'Battery cycling', 'Maccor', 'Python'],
    url='https://github.com/shriyachallam/maccorcyclingdata',
    download_url='https://pypi.org/project/maccorcyclingdata/',
    include_package_data=True
)

install_requires = [
    #list all dependencies needed
    'pandas>=1.0.1',
    'numpy>=1.18.1',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
