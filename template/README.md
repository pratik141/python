file_render
=============

Load data variables from YAML-formatted files for Jinja2 template and rendering to the standard output file.

Installation
------------

.. code-block:: bash

   ./setup.py install

Usage
-----

.. code-block:: bash

    file_render -t <template file name> -d <data file name> -o <output file name>

Example
-------

Template file ``template.j2``:

.. code-block:: yaml

    ---
    userService:
      - name: {{ name }}
        age: {{ age }}

data file ``data.yml``:

.. code-block:: yaml

    ---
    name: abc
    age: 25

Rendering the template file:

.. code-block:: bash

  file_render -t template.j2  -d data.yml -o output.yml

Result:

.. code-block:: yaml
  ---
  userService:
    - name: abc
      age: 25

