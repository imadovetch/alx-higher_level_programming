#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes object information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *py_object)
{
    char *byte_string;
    long int size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(py_object))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(py_object))->ob_size;
    byte_string = ((PyBytesObject *)py_object)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", byte_string);

    if (size >= 10)
        limit = 10;
    else
        limit = size + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
        if (byte_string[i] >= 0)
            printf(" %02x", byte_string[i]);
        else
            printf(" %02x", 256 + byte_string[i]);

    printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @py_object: Python Object
 * Return: no return
 */
void print_python_list(PyObject *py_object)
{
    long int size, i;
    PyListObject *list;
    PyObject *item;

    size = ((PyVarObject *)(py_object))->ob_size;
    list = (PyListObject *)py_object;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        item = ((PyListObject *)py_object)->ob_item[i];
        printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
