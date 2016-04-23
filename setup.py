import os

from setuptools import find_packages
from setuptools import setup


setup(
    name='docopt-example',
    version=(open(os.path.join(os.path.dirname(__file__),
                               'app',
                               'version.txt'))
             .read().strip()),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['docopt'],
    entry_points={
        'console_scripts': [
            'docopt-example = app.main:main',
        ],
    },
)
