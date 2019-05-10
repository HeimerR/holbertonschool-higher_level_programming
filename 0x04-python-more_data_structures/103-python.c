#include <Python.h>
#include <stdio.h>
#include <strings.h>
/**
 *  print_python_bytes - prints some basic info about Python lists.
 * @p: pointer to a object
 * Return: no return
**/
void print_python_bytes(PyObject *p)
{
	int size;
	int i = 0;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size =  (int)(assert(PyBytes_Check(p)), (((PyVarObject *)(p))->ob_size));
	printf("  size: %d\n", size);
	str =  PyBytes_AsString(p);
	printf("  trying string: %s\n", str);
	if (size >= 10)
		size = 9;
	printf("  first %d bytes:", size + 1);
	while (i <= size)
	{
		printf(" %02x", (unsigned int) *str++ & 0xFF);
		i++;
	}
	printf("\n");

}
/**
 * print_python_list - prints some basic info about Python lists.
 * @p: pointer to a object
 * Return: no return
**/
void print_python_list(PyObject *p)
{
	int sizeobj;
	int i;
	PyObject *p2;

	printf("[*] Python list info\n");
	sizeobj = (((PyVarObject *)(p))->ob_size);
	printf("[*] Size of the Python List = %d\n", sizeobj);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < sizeobj; i++)
	{
		p2 = (((PyListObject *)(p))->ob_item[i]);
		printf("Element %d: %s\n", i, ((p2)->ob_type)->tp_name);
		if (strcmp(((p2)->ob_type)->tp_name, "bytes") == 0)
		{
			print_python_bytes(p2);
		}
	}
}
