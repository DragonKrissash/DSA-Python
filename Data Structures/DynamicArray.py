class DynamicArray:

    def __init__(self,cap=1):
        self.__capacity=cap
        self.__size=0
        self.__data=[None]*cap
        self.__resizeFactor=2

    #Function to resize
    def setResizeFactor(self,rf):
        self.__resizeFactor=rf

    #Function to check index
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

    def __str__(self):
        if self.isEmpty():
            return "[]"
        else:
            l=[]
            for i in range(self.__size):
                l.append(self.__data[i])
            return ", ".join(map(str,l))

    #Function to resize as per user's choice
    def __resize(self):
        new_array=[None]*self.__resizeFactor*self.__size
        for i in range(self.__size):
            new_array[i]=self.__data[i]
        self.__capacity=self.__resizeFactor*self.__capacity
        self.__data=new_array

    #Function to check if empty
    def isEmpty(self):
        return self.__size==0

    #Function to append at last
    def append(self,val):
        if self.__size<self.__capacity:
            self.__data[self.__size]=val
            self.__size+=1
        else:
            self.__resize()
            self.append(val)

    #Function to append at any index
    def addAt(self,index,data):
        if index>self.__size:
            raise Exception("Index out of bounds!")
        if self.isEmpty() or self.__size==index:
            self.append(data)
        else:
            if self.__size<self.__capacity:
                for i in range(self.__size,index-1,-1):
                    self.__data[i]=self.__data[i-1]
                self.__data[index]=data
                self.__size+=1
            else:
                self.__resize()
                self.addAt(index,data)

    #Function to pop at last index
    def pop(self):
        if self.isEmpty():
            raise Exception("Empty list!")
        else:
            self.__data[self.__size-1]=None
            self.__size-=1

    #Function to remove from any index
    def removeAt(self,index):
        if self.isEmpty():
            raise Exception("Empty array!")
        elif index>=self.__size:
            raise Exception("Index Out of bounds!")
        else:
            if index==self.__size-1:
                self.pop()
            else:
                for i in range(index,self.__size):
                    self.__data[i]=self.__data[i+1]
                self.__size-=1

    #Function to rotate once
    #Used in rotate k times 
    def rotateOnce(self):
        if self.isEmpty():
            raise Exception("Empty array!")
        else:
            if self.__size==1:
                pass
            else:
                x=self.__data[self.__size-1]
                for i in range(self.__size-1,0,-1):
                    self.__data[i]=self.__data[i-1]
                self.__data[0]=x

    #Function to rotate k times
    def rotate(self,k):
        if self.isEmpty():
            raise Exception("Empty array!")
        else:
            for i in range(k):
                self.rotateOnce()

    #Function to reverse
    def reverse(self):
        if self.isEmpty():
            raise Exception("Empty array!")
        else:
            l=[]
            for i in range(self.__size-1,-1,-1):
                l.append(self.__data[i])
            self.__data=l
            del(l)

    #Function to add at first
    def prepend(self,data):
        if self.isEmpty():
            raise Exception("Empty array!")
        else:
            self.addAt(0,data)

    #Function to merge to arrays
    def merge(self,arr):
        if self.isEmpty():
            raise Exception("Empty array!")
        if len(arr)==0:
            pass
        else:
            n1=len(arr)
            n2=self.__size
            i,j=0,0
            res_arr=[]
            while i+j<n2+n1:
                if i==n1:
                    res_arr.append(self.__data[j])
                    j+=1
                elif j==n2:
                    res_arr.append(arr[i])
                    i+=1
                else:
                    if arr[i]<self.__data[j]:
                        res_arr.append(arr[i])
                        i+=1
                    else:
                        res_arr.append(self.__data[j])
                        j+=1
            self.__data=res_arr
            self.__size+=len(arr)
            del(res_arr)

    #Function to interleave to arrays
    def interleave(self,arr):
        if self.isEmpty():
            raise Exception("Empty array!")
        if len(arr)==0:
            pass
        else:
            l=[]
            n1=len(arr)
            n2=self.__size
            i,j=0,0
            while i+j<n1+n2:
                if i==n1:
                    l.append(self.__data[j])
                    j+=1
                elif j==n2:
                    l.append(arr[i])
                    i+=1
                else:
                    l.append(self.__data[j])
                    l.append(arr[i])
                    i+=1
                    j+=1
            self.__data=l
            del(l)
            self.__size+=len(arr)

    #Function to get middle element
    def midElement(self):
        if self.isEmpty():
            raise Exception("Empty array!")
        else:
            return self.__data[(self.__size)//2]

    #Function to search for x
    def find(self,x):
        if self.isEmpty():
            raise Exception("Empty array!")
        else:
            for ind,i in enumerate(self.__data):
                if i==x:
                    return ind
            return -1

    #Function to split the array at given index
    def split(self,ind):
        if self.isEmpty():
            raise Exception("Empty array!")
        else:
            l2=DynamicArray()
            for i in range(ind,self.__size):
                l2.append(self.__data[i])
                self.__data[i]=None
            self.__size-=len(l2)
            l1 = DynamicArray()
            for i in range(ind):
                l1.append(self.__data[i])
            return (l1,l2)

arr=DynamicArray()
arr.append(2)
arr.append(4)
arr.append(5)
arr.append(6)
print(arr)
# arr2=DynamicArray()
# arr2.append(3)
# arr2.append(5)
# print(arr2)
# arr.interleave(arr2)
arr1,arr2=arr.split(4)
print(arr1," ",arr2)
