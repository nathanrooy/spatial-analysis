#include "Python.h"
#include "haversine.h"
#include "vincenty.h"

/* Docstrings */
static char module_docstring[] =
    "A collection of scripts for the analysis of spatial data...";
static char haversine_docstring[] =
    "Haversine function";

    
/* Available functions */
static PyObject *spatial_haversine(PyObject *self, PyObject *args);
static PyObject *spatial_vincenty_inv(PyObject *self,  PyObject *args);


/* Module specification */
static PyMethodDef module_methods[] = {
    {"haversine",    spatial_haversine,    METH_VARARGS, haversine_docstring},
    {"vincenty_inv", spatial_vincenty_inv, METH_VARARGS, haversine_docstring},
    {NULL, NULL, 0, NULL}
};


/* Initialize the module */
PyMODINIT_FUNC PyInit__spatial(void)
{
    
    PyObject *module;
    static struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "_spatial",
        module_docstring,
        -1,
        module_methods
    };
    
    module = PyModule_Create(&moduledef);
    if (!module) return NULL;

    return module;
}


static PyObject *spatial_haversine(PyObject *self, PyObject *args)
{
    double x1, x2, y1, y2;
    
    if (!PyArg_ParseTuple(args, "dddd", &x1, &y1, &x2, &y2))
        return NULL;
    
    double ans = haversine(x1, y1, x2, y2);
    return PyFloat_FromDouble(ans);

}


static PyObject *spatial_vincenty_inv(PyObject *self, PyObject *args)
{
    double x1, x2, y1, y2, tol;
    unsigned int i;
    
    if (!PyArg_ParseTuple(args, "ddddId", &x1, &y1, &x2, &y2, &i, &tol))
        return NULL;
    
    double ans = vincenty_inv(x1, y1, x2, y2, i, tol);
    return PyFloat_FromDouble(ans);

}
