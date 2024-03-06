class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self)-> float:
        return 1 * self.__base + 1 * self.__height
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return 3 * self.__base + 3 * self.__height

 
 triangle_1 = Rectangle(5,10)
 print("The area of the rectangle is", get)
#YOUDO>  create two rectangles.  print their base, height, perimeter, and area
#using only the methods not the fields/property/attributes
