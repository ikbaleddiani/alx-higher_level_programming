#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
        PyListObject *list_object = (PyListObject *)p;
	int i, length;

        printf("[*] Size of the Python List = %d\n", (int)PyList_Size(p));
        printf("[*] Allocated = %lu\n", list_object->allocated);
	length = (int)PyList_Size(p);
        for (i = 0; i < length; i++)
        {
		printf("Element %d: %s\n", i, list_object->ob_item[i]->ob_type->tp_name);
        }
}
