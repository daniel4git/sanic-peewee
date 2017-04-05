from distutils.core import setup

with open('requirement.txt',"r") as f:
    required = f.read().splitlines()
with open('README.rst',"r") as readme:
    long_description = readme.read()
setup(
    name='sanic-peewee',
    version='0.0.1',
    author='Huang Sizhe',
    author_email='hsz1273327@gmail.com',
    packages=['sanic_peewee'],
    license='BSD',
    description='a simple sanic extension for using async-peewee',
    long_description=long_description,
    install_requires=required,
    )
