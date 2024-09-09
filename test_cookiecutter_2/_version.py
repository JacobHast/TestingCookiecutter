def _get_version() -> str:
    from pathlib import Path

    import versioningit

    import test_cookiecutter_2

    test_cookiecutter_2_path = Path(test_cookiecutter_2.__file__).parent
    return versioningit.get_version(project_dir=test_cookiecutter_2_path.parent)


__version__ = _get_version()
