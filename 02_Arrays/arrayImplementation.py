import ctypes
#ctypes is a foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared libraries.

class array:
    """
    array implementation

    """
    def __init__(self):
        self.item_count = 0
        self.array_size = 1
        self.primary_array = self.create_array(self.array_size)

    def create_array(self, array_size):
        return (array_size*ctypes.py_object)( )

    def list_of_elements(self):
        for element in self.primary_array:
            return " ".join(str(self.primary_array[x] for x in range(self.item_count)))

    def length(self):
        return self.item_count

    def get_element(self, element_index):
        if not 0 <= element_index < self.item_count:
            return IndexError('index out of range')
        return self.primary_array[element_index]
    
    def insert(self, item):
        if self.item_count == self.array_size:
            self.enlarge_array(2*self.array_size)
        self.primary_array[self.item_count] = item
        self.item_count += 1    

    def enlarge_array(self, new_size):
        secondary_array = self.create_array(new_size)
        for i in range(self.item_count):
            secondary_array = self.primary_array[i]
        self.primary_array = secondary_array
        self.array_size = new_size

    def delete(self,element_index ):
        if 0 > element_index or  element_index > self.item_count -1:
            return IndexError('Index out of range')

        while 0 <= element_index < self.item_count -1:
            self.primary_array[element_index] = self.primary_array[element_index + 1]
            element_index += 1
        self.item_count -= 1

    
    
a = array
a.insert(a, 2)


a.list_of_elements(a)