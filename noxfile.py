import nox


@nox.session(python=["3.8", "3.9"])
def tests(session):
    args = session.posargs or ["--cov"]
    session.install(".", "pytest", "pytest-cov", "coverage[toml]", "pytest-mock")
    # session.run("pytest", external=True)
    session.run("pytest", *args)


locations = "read_stream", "tests", "noxfile.py"


@nox.session(python=["3.8", "3.9"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    # session.install("flake8-import-order")
    session.run("flake8", *args)
