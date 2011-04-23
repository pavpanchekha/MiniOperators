MiniOperators for Python
========================

This library makes it almost trivial to add extended operators to the python
language, or to transform existing functions into binary operators. For
example, one might take the function ``compose``::

    def compose(f, g):
        return lambda *args, **kwargs: f(g(*args, **kwargs))

And turn it into an operator, ``|compose|``::

    compose = MiniOperator(compose)

Then, the operator can be used as a binary operator [#]_::

    f = math.sqrt  |compose|  (lambda x: x**2 + 1)
    f(0) # 1.0

If one consistently uses this ``|<name>|`` notation and parenthesises
arguments, no problems should arise [#]_.

Furthermore, the operator thus created will support overriding through the
standard Python convention of ``__<name>__`` and ``__r<name>__`` special
methods.

Documentation
-------------

The ``MiniOperator`` constructor can be called in three ways.
``MiniOperator(f)`` creates an operator named ``f`` that uses ``f`` as its
default operation [#]_. A name can also be explicitely passed:
``MiniOperator(name, f)``, where ``name`` is a string, will create an operator
named ``name`` that uses ``f`` as a default operation. Finally, one can create
an operator without specifying a default method: ``MiniOperator(name)``, where
``name`` is a string, will result in an operator that will throw a
``NotImplementedError`` when used on most arguments. However, a class will be
able to explicitely override ``__<name>__`` or ``__r<name>__`` to support this
operator.

.. rubric:: Footnotes

.. [#] Of course, the initial function must be binary --- that is, it must take
    two arguments --- and other obvious restrications apply as well.
.. [#] The author would like to suggest using two spaces around the operator
    and to take special care parenthesizing expressions.
.. [#] That is, the name is derived from the ``__name__`` of the passed function.
    The author suggests not overrelying on this form.
