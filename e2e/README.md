# Environment setup

Python 3 is required to run the tests. Use venv to create a virtual environment in the e2e folder:

```python -m venv {env_name}```

To activate the environment:

```source {env_name}/bin/activate```

To deactivate the environemnt:

```source deactivate```

# Install dependencies

Once the environment is active, install library dependencies:

```pip install -r requirements.txt```

Also install the browser packages for playwright:

```playwright install```

# Running tests

To run all tests simply use:

```pytest```
