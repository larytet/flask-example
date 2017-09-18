import setuptools

setuptools.setup(
    name='yalas',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)