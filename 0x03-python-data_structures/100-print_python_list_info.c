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
	int i;
	PyObject *p2;

	sizeobj = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", sizeobj);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < sizeobj; i++)
	{
		p2 = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(p2)->tp_name);
	}
}
