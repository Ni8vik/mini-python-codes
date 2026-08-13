
class foodrating:
      def __init__(self, food, cuisines, rating):
            self.food = food
            self.cuisines = cuisines
            self.rating = rating
      
      def changerating(self, food, newrating):
            self.rating = newrating
      
      def hightestrated(self, cuisine):
            pass
      
fd = foodrating("egg", "africanano", 14)

fd.changerating(None, 17)

print(fd.rating)