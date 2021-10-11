from distutils.core import setup

setup(
    name='analyzeMFT',
    version='3.0.0',
    author='David Kovar, INCIDE Digital SL',
    author_email='tecnico@incide.es',
    packages=['analyzemft'],
    url='http://github.com/IncideDigital/analyzeMFT',
    license='LICENSE.txt',
    description='Analyze the $MFT from a NTFS filesystem.',
    long_description=open('README.txt').read(),
    scripts=['analyzeMFT.py']
)
