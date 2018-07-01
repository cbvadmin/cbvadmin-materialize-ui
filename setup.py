from setuptools import setup
from cbvadmin_materialize_ui import __version__

setup(
    name='cbvadmin-materialize-ui',
    version=__version__,
    description='Materialize CSS template for CBVadmin',
    long_description=open('README.rst').read(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=['admin', 'django'],
    author='roldaojr',
    author_email='roldaogjr@gmail.com',
    url='https://github.com/roldaojr/cbvadmin-materialize-ui',
    license='MIT',
    packages=['cbvadmin_materialize_ui'],
    include_package_data=True,
    install_requires=[
        'Django>=2.0',
        'django-crispy-forms>=1.6',
        'materialize_css_forms>=1.0',
    ]
)
