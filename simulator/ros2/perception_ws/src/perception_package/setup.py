
from setuptools import setup
from glob import glob
import os

package_name = 'perception_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bhavana',
    maintainer_email='bhavana@example.com',
    description='Autonomous driving perception ROS 2 package',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'perception_node = perception_package.perception_node:main',
        ],
    },
)
