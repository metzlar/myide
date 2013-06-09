from setuptools import setup
import sys

if 'register' in sys.argv or 'upload' in sys.argv:
    raise Exception('I don\'t want to be on PyPI (yet)!')

setup(
    name='myide',
    version='0.1',
    license='BSD',
    author='Ivan Metzlar',
    author_email='metzlar@gmail.com',
    description='My Python IDE',
    py_modules=['myide'],
    zip_safe=False,
    platforms='any',
    include_package_data=True,

)