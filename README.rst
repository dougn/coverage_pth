
coverage_pth - install a .pth file to site-packages to enable coverage.py
==========================================================================

The instructions for `starting coverage.py automatically <http://nedbatchelder.com/code/coverage/api.html#h_starting_coverage_automatically>`_
includes creating a ``.pth`` file with the contents:

.. code::
    
    import coverage; coverage.process_startup()
    
The project only contains this .pth file so you can easilly have this enabled
via a pip install. The wheel files generated are platform and python specific
due to the limitations of wheel files, where the relative directory for
site-packages needs to be determined at wheel building time, not install time.
The directory is dependent on the version of python and the platform you are
on.

    