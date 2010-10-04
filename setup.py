from setuptools import setup, find_packages

setup(
    name='django-countryip',
    version=__import__('countryip').__version__,
    description='Provides a utility to import countries and IP ranges into your database via the Maxmind csv country database.',
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Gap Adventures',
    author_email='websupport@gap.ca',
    url='http://http://github.com/gapadventures/django-countryip',
    download_url='http://github.com/gapadventures/django-countryip',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)