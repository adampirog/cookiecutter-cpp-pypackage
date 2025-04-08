#include "Pet.hpp"

Pet::Pet(const std::string& name) : name(name) {}
void Pet::setName(const std::string& name_) { name = name_; }
const std::string& Pet::getName() { return name; }
