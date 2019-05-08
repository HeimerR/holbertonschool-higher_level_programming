#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to a object
 * Return: no return
**/
void print_python_list_info(PyObject *p)
{
	int sizeobj;

	sizeobj = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", sizeobj);
}
