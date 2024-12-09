===============
Old Test Verify
===============

Substitutions
-------------

Here is test from the |doc_version| branch.

Trying Intersphinx
------------------

.. To scan stuff run commands to see what can be addressed "python -msphinx.ext.intersphinx https://docs.python.org/3/objects.inv > objectsFile.txt"

This is an interesting item and here is a link to (py:function) :external+python:py:func:`min`

This was the default example: :external+python:py:class:`zipfile.ZipFile`

This thing was the default example: :external+python:std:doc:`library/csv`

:external+python:std:doc:`howto/functional`

:external+python:std:doc:`library/functional`

Specify a module (py:module) :external+python:py:mod:`csv`

.. Specify a label :external+python:std:label:`assert`

Specify a label :ref:`assert <python:assert>`

Specify a term :external+python:std:term:`awaitable`

Test alternate format example:  :ref:`comparison manual <python:comparisons>` 


The Actual Code
---------------
.. automodule:: old_test_verify
    :members:
    :undoc-members:

Inheritance Diagrams
--------------------
.. inheritance-diagram:: FooFitnessFunction

Graphvis Diagrams
-----------------

.. For more Graphvis info see https://graphviz.org/pdf/dot.1.pdf     https://graphviz.org/docs/layouts/

.. Usually, use Layout as "neato" or "dot" if there is an issue

.. graphviz::

   digraph foo {
      "bar" -> "baz";
   }

.. graph:: example_graph
    :alt: This is a sample graph alt text
    :caption: Caption for the graph
    :layout: neato
    :align: center
    :name: This is the name of the graph

    "a" -- "b"
    "b" -- "c"
    "c" -- "d"
    "a" -- "c" -- "e" -- f -- d

.. digraph:: example_diagraph
    :name: This is the name.
    :alt: This is the diagraph built
    :caption: This is the sample graph caption
    :align: right
    :layout: dot

    "c" [label="Item C", href="https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html", target="_top"]

    "a" -> "b"
    "b" -> "c" -> "b"
    "d" -> "f" -> "g" -> "d"
