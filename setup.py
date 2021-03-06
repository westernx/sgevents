from setuptools import setup, find_packages

setup(

    name='sgevents',
    version='0.1-dev',
    description='A safe Shotgun event daemon',
    url='http://github.com/westernx/sgevents',
    
    packages=find_packages(exclude=['build*', 'tests*']),
    
    author='Mike Boers',
    author_email='sgevents@mikeboers.com',
    license='BSD-3',
    
    install_requires=[
        # one of `sgapi` or `shotgun_api3` is required
    ],

    entry_points={
        'console_scripts': '''
            sgevents-daemon = sgevents.commands.daemon:main
            sgevents-dispatch = sgevents.commands.dispatch:main
        ''',
    },

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    
)
