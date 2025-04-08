from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__package_name__ = "{{ cookiecutter.package_name }}"
__version__ = "0.1.0"

ext_modules = [
    Pybind11Extension(
        __package_name__,
        [
            f"{__package_name__}/bindings/bindings.cpp",
            f"{__package_name__}/Pet.cpp",
        ],
        define_macros=[("VERSION_INFO", __version__)],
    ),
]

setup(
    name=__package_name__,
    version=__version__,
    author="Adam Pirog",
    author_email="pirog.adam@gmail.com",
    url="https://github.com/adampirog",
    description="{{ cookiecutter.short_project_description }}",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.11",
    extras_require={"dev": ["pytest", "isort", "black", "pylint"]},
)
