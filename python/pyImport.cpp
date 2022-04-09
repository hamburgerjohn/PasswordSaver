#include "database.h"
#include <pybind11/pybind11.h>
//#include <pybind11/stl.h>


PYBIND11_MODULE(database, handle){
    handle.doc() = "Module for import c++";

    pybind11::class_<Database>(
        handle, "Database"
    )
    .def(pybind11::init<const char*, const char*, const char*, const char*>())
    .def(pybind11::init<>())
    .def("Insert", &Database::Insert)
    .def("Remove", &Database::Remove)
    .def("Update", &Database::Update)
    .def("SetTable", &Database::SetTable)
    .def("CreateTable", &Database::CreateTable)
    .def("DropTable", &Database::DropTable)
    .def("GetTable", &Database::GetTable)
    .def("GetPassword", &Database::GetPassword);

}
