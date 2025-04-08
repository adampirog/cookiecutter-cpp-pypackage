import re

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"


def check_package_name():
    package_name = "{{ cookiecutter.package_name }}"

    if not re.match(MODULE_REGEX, package_name):
        raise ValueError(f"{package_name} is not a valid Python package name")


def main():
    check_package_name()


if __name__ == "__main__":
    main()
