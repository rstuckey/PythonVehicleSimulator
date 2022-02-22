from setuptools import setup

setup(name='PythonVehicleSimulator',
      version='0.1',
      description="The Python Vehicle Simulator is a supplement to the Matlab MSS (Marine Systems Simulator) toolbox. It includes models for autonomous underwater vehicles (AUVs), unmanned surface vehicles (USVs), and ships. The vehicle models are based on the MSS vessel models located in /MSS/VESSELS/ catalogue. Each vehicle is modeled as an object in Python and the vehicle class has methods for guidance, navigation and control.",
      url='https://github.com/cybergalactic/PythonVehicleSimulator',
      author='Thor I. Fossen',
      author_email='thor.fossen@ntnu.no',
      license='MIT',
      packages=['pythonvehiclesimulator'],
      zip_safe=False)
