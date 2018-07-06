Sphinx Test project
===================

This documentation aims to provide an example of how to properly document 
a Python package using the following technologies:

- Sphinx_ with the following 
  extensions:

  - `Autodocs \
    <https://sphinx.readthedocs.io/en/master/usage/extensions/autodoc.html>`_
    to document `Python's docstrings \
    <https://www.python.org/dev/peps/pep-0257/>`_
  - `Napoleon \
    <https://sphinx.readthedocs.io/en/master/usage/extensions/napoleon.html>`_
    to use `Google docstrings style \
    <https://github.com/google/styleguide/blob/gh-pages/pyguide.md#381-\
    docstrings>`_
  - `Doctest \
    <https://sphinx.readthedocs.io/en/master/usage/extensions/doctest.html>`_
    to test if the code in the comments do return what is expected

.. _Sphinx: https://sphinx.readthedocs.io/en/master/

In order for the documentation to be visually friendly, we use the 
`Read the docs <https://pypi.org/project/sphinx_rtd_theme/>`_ theme

We also use the following notation for documenting types and use static typing
checkers like `MyPy <https://mypy.readthedocs.io/en/latest/>`_

- `PEP 484 for type hints and documentation \
  <https://www.python.org/dev/peps/pep-0484/>`_

How to
------
In order to create the documentation, as Sphinx_ mentions in their getting 
started page, you have a ``Makefile`` for UNIX-like systems and a ``make.bat``
file for Windows systems so in order to build the documentation locally you
just have to execute the following command:

.. code-block:: bash
   
   make html

To build the documentation in HTML. Then just open the |index.html file|_ in
your browser and you're ready to go.

.. |index.html file| replace:: ``index.html`` file
.. _`index.html file`: https://github.com/davidlj95/sphinx-test/tree/master/docs/_build/html/index.html

Repository
----------

All this code is located at a `GitHub repository \
<https://github.com/davidlj95/sphinx-test>`_

Documentation
-------------

This documentation uses code from a `GitHub project \
<https://github.com/BTCAssessors/bitcoin-framework/>`_ in order to see how well
it gets documented. Indeed this sample project was made to be able to document
that project. This project contains just one module called ``bitcoin``

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   self
   bitcoin
