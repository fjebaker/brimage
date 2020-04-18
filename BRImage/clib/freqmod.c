#include <freqmod.h>

#include <math.h>
#include <stdio.h>

PyObject* array_to_list(double array[], int length) {
	PyObject* list = PyList_New(length);
	for (int i = 0; i < length; i++) {
		// printf("i = %d; index = %lf\n", i, array[i]);
		PyList_SetItem(list, i, PyFloat_FromDouble(array[i]));
	}
	return list;
}

PyObject* test_func(PyObject* self, PyObject* args) {
	double array[] = {1, 2, 3, 4, 6};

	PyObject* list = array_to_list(array, 5);
	return list;
}

double remap(double x, double s1, double s2, double d1, double d2) {
	return (((x - s1) * (d2 - d1)) / (s2 - s1)) + d1;
}

PyObject* freqmod_row(PyObject* self, PyObject* args) {
	PyObject* iterator;
	PyObject* item;
	PyObject* new_row;
	double x;
	double val;

	int width;
	double integral = 0;
	double runningmod = 0;
	double min_phase;
	double max_phase;
	double omega;

	if (!PyArg_ParseTuple(args, "Oidd", 
			&iterator, 
			&width, 
			&max_phase, 
			&omega)) {
		return NULL;
	}

	new_row = PyList_New(width);
	min_phase = -max_phase;

	if (!PyIter_Check(iterator)) {
		iterator = PyObject_GetIter(iterator);
		if (iterator == NULL) {
			PyErr_SetString(PyExc_TypeError,
				"Argument is not iterable.");
			return NULL;
		}
	}

	for (int i = 0; i < width; i++) {
		item = PyIter_Next(iterator);
		x = PyFloat_AsDouble(item);
		Py_DECREF(item);

		x = remap(x, 0, 255, min_phase, max_phase);
		integral += x;
		x = cos(((omega * i) + integral) * 0.5);

		val = fabs(x - runningmod);
		runningmod = x;

		val = remap(2 * (val - omega), min_phase, max_phase, 0, 255);

		PyList_SET_ITEM(new_row, i, PyFloat_FromDouble(val));
	}
	Py_DECREF(iterator);

	return new_row;
}