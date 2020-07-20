file_render
=============

Load data variables from YAML-formatted files for Jinja2 template and rendering to the standard output file.

Installation
------------

``` bash

   ./setup.py install
```
Usage
-----

``` bash

    file_render -t <template file name> -d <data file name> -o <output file name>
``` 

Example
-------

Template file ``template.j2``:

``` yml

    ---
    userService:
      - name: {{ name }}
        age: {{ age }}
```

data file ``data.yml``:

``` yml

    ---
    name: abc
    age: 25
```
Rendering the template file:

``` bash

  file_render -t template.j2  -d data.yml -o output.yml
``` 
Result:

```yml
  ---
  userService:
    - name: abc
      age: 25
```
