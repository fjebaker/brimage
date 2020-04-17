#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include "freqmod.h"

static PyMethodDef brimage_methods[] = {
	{ 
		"freqmod_row", freqmod_row, METH_VARARGS, "Applies frequency modulation to a single row."
	},
	{
		"testfunc", test_func, METH_VARARGS, "Testfunc."
	},
	{NULL, NULL, 0, NULL},
};

static struct PyModuleDef brimage_module = {
	PyModuleDef_HEAD_INIT,
	"algorithms",
	NULL,
	-1,
	brimage_methods,
};

// init the module
PyMODINIT_FUNC PyInit_algorithms(void) {
	return PyModule_Create(&brimage_module);
}