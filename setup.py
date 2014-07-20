from setuptools import setup, find_packages


setup(
    name='bassh',
    version='0.1',
    install_requires=(
    ),
    packages=find_packages('src/'),
    package_dir={'': 'src', },
    dependency_links = (
        ),
    scripts=(
        'scripts/bassh',
        'scripts/bassh.sh',
    ),
)


