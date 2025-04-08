#include <pybind11/pybind11.h>

#include "../Pet.hpp"
#include "../utils.cpp"

namespace py = pybind11;

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

PYBIND11_MODULE({{cookiecutter.package_name}}, m) {
  m.doc() = R"pbdoc(
        {{ cookiecutter.short_project_description }}
    )pbdoc";

  py::class_<Pet>(m, "Pet")
      .def(py::init<const std::string&>())
      .def("setName", &Pet::setName)
      .def("getName", &Pet::getName);

  m.def("add", &add, "A function that adds two numbers");
  m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
}
