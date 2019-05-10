#include <Python.h>
#include <stdio.h>
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
	size =  (int)(assert(PyBytes_Check(p)),(((PyVarObject*)(p))->ob_size));
	printf("size: %d\n", size);
	str =  PyBytes_AsString(p);
	printf("trying string: %s\n", str);
	if (size > 11)
		size = 9;
	printf("first %d bytes: ", size + 1);
	while(*str || i < 10)
 		printf("%02x ", (unsigned int) *str++);
		i++;
	printf("\n");

}
/**
 * print_python_list - prints some basic info about Python lists.
 * @p: pointer to a object
 * Return: no return
**/
void print_python_list(PyObject *p)
{
	(void)p;


}
