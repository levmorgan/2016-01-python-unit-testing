These are the companion files for the Python Unit Testing Tutorial. These include:

Unit Testing Project 1.ipynb: The Jupyter notebook used in the presentation
python_unit_testing_1.py: A simple example of the unittest module
python_unit_testing_2.py: A more complicated example, with setUp and tearDown methods

The .py files have been set up so that the unit tests can be run simply by using the Python 
interperter:

cd unit_testing_demo; python step_1_test.py


But you can run unit tests from the command line in a variety of ways. 
You can call a whole module, a test case, or just one test method: 
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method