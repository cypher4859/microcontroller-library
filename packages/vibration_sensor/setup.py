from setuptools import setup, find_packages

setup(
    name='vibration_sensor',
    version='0.1.0',    
    description='Module for handling detection of vibration and reacting.',
    author='cypher4859',
    package_dir={"": "vibration_sensor_node"},
    packages=find_packages("vibration_sensor_node"),
)