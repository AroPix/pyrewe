import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyrewe',
    author='AroPix',
    author_email='aropix@tutanota.com',
    description='REWE API wrapper',
    keywords='api, pypi, wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AroPix/pyrewe',
    project_urls={
        'Documentation': 'https://github.com/AroPix/pyrewe',
        'Bug Reports': 'https://github.com/AroPix/pyrewe/issues',
        'Source Code': 'https://github.com/AroPix/pyrewe',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
    extras_require={
        'dev': ['check-manifest']
    }
)