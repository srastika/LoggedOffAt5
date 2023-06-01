from setuptools import setup

setup(
    name='weather_forecast',
    version='1.0.0',
    description='',
    author='logged_out_at_5',
    packages=['weather_forecast'],
    install_requires=[],
        entry_points={
        'console_scripts': [
            'weather_forecast=weather_forecast.weather_forecast:main',
        ],
    },
)