====
cumulus-post-map-payload-grouping
====
This is the python code for the lambda `cumulus-post-map-payload-grouping`.
It simply takes in the output from a `Distributed Mode AWS Step Function Map <https://docs.aws.amazon.com/step-functions/latest/dg/use-dist-map-orchestrate-large-scale-parallel-workloads.html>`_ and obtains the status of each mapped execution.

Required Input
====
Output of the map; this function does not utilize the cumulus library so is relatively bare bones to other lambdas

Build (as a zip to load to AWS Lambda)
====
`This <https://chariotsolutions.com/blog/post/building-lambdas-with-poetry/>`_ page contains some good info on the overall "building a zip with poetry that's compatible with AWS Lambda".

Auto build script
----
TL;DR ::

    sh ./build.sh;

to run the following commands in order and build the cumulus-pre-map-payload-grouping.zip artifact

Manual build
----
This command creates the ``dist/`` folder::

    poetry build

This command downloads the dependency files from the just created .whl file, along with the lambda_handler function in ``cumulus_post_map_payload_grouping/cumulus_post_map_payload_grouping.py``, and places them in the ``package`` folder::

    poetry run pip install --upgrade -t package dist/*.whl

Note that **moto** is not being pulled in. I've specifically excluded it via having **moto** as ``tool.poetry.dev-dependencies`` only (via the ``pyproject.toml`` file)

The last command used is::

    cd package ; zip -r ../artifact.zip . -x '*.pyc'

Which zips and creates the ``artifact.zip`` file, containing all files found in ``package/`` excluding .pyc files

Then upload ``artifact.zip`` to any location you plan to use it

* Upload directly as a lambda with ``aws lambda update-function-code``
* Upload to your AWS S3 ``lambdas/`` folder so that your Cumulus Terraform Build can use it