from setuptools import setup, find_packages

setup(name='ezzybot',
      version='1.3.4',
      description="Python IRC framework",
      url='https://ezzybot.zzirc.xyz',
      author='EzzyBot team',
      author_email='me@lukej.me',
      license='GNU',
      packages=find_packages(),
      install_requires=['thingdb', 'pysocks', 'requests', 'ecdsa'],
      include_package_data=True,
      zip_safe=False)
