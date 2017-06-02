from setuptools import setup

setup(name='ittools',
      version='1.0',
      description='Tools to measure entropy',
      url='https://github.com/Fuminides/Python-Entropy-Tools',
      author='Miguel Aguilera',
      license='MIT',
      packages=['ittools'],
      install_requires=[
          'numpy',
      ],

      zip_safe=False)