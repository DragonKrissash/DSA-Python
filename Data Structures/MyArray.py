class MyArray:

    def __init__(self,cap:int):
        self.__capacity=cap
        self.__size=0
        self.__data=[None]*cap

    def __isvalid(self,ind):
        if 0 <= ind < self.__size:
            return True
        else:
            return False

    def __getitem__(self, ind)-> int:
        if self.__isvalid(ind):
            return self.__data[ind]
        else:
            raise IndexError("Index out of bounds!")

    def __setitem__(self, ind,val):
        if self.__isvalid(ind):
            self.__data[ind]=val
        else:
            raise IndexError('Index out of bounds!')

    def __len__(self):
        return self.__size

    def __resize(self):
        new_array=[None]*2*self.__size
        for i in range(self.__size):
            new_array[i]=self.__data[i]
        self.__capacity=2*self.__capacity
        self.__data=new_array

    def append(self,val):
        if self.__size<self.__capacity:
            self.__data[self.__size]=val
            self.__size+=1
        else:
            self.__resize()
            self.append(val)

arr=MyArray(5)
arr.append(4)
arr.append(2)
arr.append(5)
for i in arr:
    print(i)
print(len(arr))
