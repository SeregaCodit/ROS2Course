from setuptools import find_packages, setup

package_name = 'l7_parameter_event_hendler'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pivden',
    maintainer_email='serega.codit@gmail.com',
    description='l7_parameter_event_hendler',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'node_with_parameters = l7_parameter_event_hendler.parameter_even_handler:main'
        ],
    },
)
