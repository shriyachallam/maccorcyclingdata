import pathlib
from setuptools import setup, find_packages
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.rst").read_text()

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
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'],
)

install_requires = [
    #list all dependencies needed
    'pandas>=1.0.1',
    'numpy>=1.18.1',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
