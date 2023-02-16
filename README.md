## py-summarizer

py-summarizer is an API that utilizes natural language processing to summarize input text.

### Running Tests

To run tests for py-summarizer, follow these commands:

```
docker-compose exec web python -m pytest
```

To disable warnings, run:

```
docker-compose exec web python -m pytest -p no:warnings
```

To run only the last failed tests, execute:

```
docker-compose exec web python -m pytest --lf
```

To run only the tests with names that match a particular string expression, use:

```
docker-compose exec web python -m pytest -k "summary and not test_read_summary"
```

To stop the test session after the first failure, run:

```
docker-compose exec web python -m pytest -x
```

If you want to enter PDB after the first failure then end the test session, run:

```
docker-compose exec web python -m pytest -x --pdb
```

To stop the test run after two failures, execute:

```
docker-compose exec web python -m pytest --maxfail=2
```

To show local variables in tracebacks, use:

```
docker-compose exec web python -m pytest -l
```

To list the 2 slowest tests, run:

```
docker-compose exec web python -m pytest --durations=2
```

Please note that docker-compose is required to run the tests.
