from setuptools import find_packages, setup

package_name = 'load_cell_filter'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ademola',
    maintainer_email='demola.oris@gmail.com',
    description='Load cell sensor filter package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'load_cell_server = load_cell_filter.load_cell_server:main',
            'load_cell_client = load_cell_filter.load_cell_client:main'
        ],
    },
)
