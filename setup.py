import setuptools

setuptools.setup(
    name="app",
    version="1.0",
    packages=['flaskr'],
    entry_points={
        'console_scripts': ['app=flaskr.app:main', ]
    },
)
