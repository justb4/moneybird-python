from distutils.core import setup

setup(
    name='moneybird',
    version='0.1.4dev',
    packages=['moneybird'],
    url='https://github.com/justb4/moneybird-python',
    license='MIT',
    author='Jan-Jelle Kester (orig), Just van den Broecke (start: 0.1.4)',
    author_email='justb4@gmail.com',
    description='MoneyBird API and OAuth client library',
    requires=['requests'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    keywords='moneybird api client oauth consumer',
)
