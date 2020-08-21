from setuptools import setup

setup(
    name='autoconvolution2x',
    #version=__version__,
    description=('Experimental audio processing by autoconvolution'),
    url='https://github.com/ajjackson/2xphases',
    author='Nasca Octavian Paul, updated/repackaged by Adam Jackson',
    author_email='a.j.jackson@physics.org',
    #long_description=long_description,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',                 
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis'
        ],
    packages=['autoconvolution2x'],
    install_requires=['numpy', 'scipy'],
    entry_points={'console_scripts': [
                      '2xautoconvolution = autoconvolution2x.autoconvolution2x:main',]}
    )
