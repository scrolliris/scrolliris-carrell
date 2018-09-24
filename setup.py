import os

from setuptools import setup, find_packages

# pylint: disable=invalid-name
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, *('doc', 'DESCRIPTION.rst'))) as f:
    DESCRIPTION = f.read()
with open(os.path.join(here, 'CHANGELOG')) as f:
    CHANGELOG = f.read()

requires = [
    'better_exceptions',
    'bleach',
    'MarkupSafe',
    'Paste',
    'PasteScript',
    'python-dotenv',
    'pyramid',
    'pyramid_assetviews',
    'pyramid_chameleon',
    'pyramid_secure_response',
]

development_requires = [
    'colorlog',
    'pycodestyle',
    'pydocstyle',
    'pylint',
    'waitress',
]

testing_requires = [
    'colorlog',
    'pytest',
    'pytest-cov',
    'pytest-mock',
    'WebTest',
]

production_requires = [
    'CherryPy',
]

setup(
    name='rapperswil_jona',
    version='0.1',
    description='',
    long_description=DESCRIPTION + '\n\n' + CHANGELOG,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web wsgi pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'development': development_requires,
        'testing': testing_requires,
        'production': production_requires,
    },
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = rapperswil_jona:main
    [console_scripts]
    rapperswil_jona_pserve = rapperswil_jona.scripts.pserve:main
    rapperswil_jona_pstart = rapperswil_jona.scripts.pstart:main
    """,
)
