try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='youtube',
    packages=['youtube'],
    version='1.0.0',
    license="GPL",
    description='',
    author='Biwin John',
    author_email='biwinjohn@gmail.com',
    url='https://github.com/biwin/python-youtube',
    download_url='https://github.com/biwin/python-youtube/',
    install_requires=['requests'],
    keywords=['youtube', 'python'],
    classifiers=[],
)
