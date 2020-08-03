from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='BattGeniePublish',
    version='0.0.1',
    description='BattGenie Python Package for Publication',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Shriya Challam',
    author_email='shriyachallam10@gmail.com',
    keywords=['Battery', 'BatteryCycling', 'BattGenie'],
    url='https://github.com/shriyachallam/BattGeniePublish',
    download_url='https://pypi.org/project/battgeniepublish/'
)

install_requires = [
    #list all dependencies needed
    'pandas',
    'numpy',
    'matlab.pyplot'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
