from setuptools import setup

setup(
    name='pltvid',
    version='0.1',
    url='https://github.com/parrt/pltvid',
    license='MIT',
    py_modules=['pltvid'],
    author='Terence Parr',
    author_email='parrt@cs.usfca.edu',
    install_requires=['matplotlib'],
    description='A simple library to capture multiple matplotlib plots as a movie.',
    keywords='matplotlib plot movie animation visualization',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Intended Audience :: Developers']
)
