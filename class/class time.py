class time:
    def __init__(self,hrs= 0,minutes= 0,sec= 0):
        self.hour = hrs
        self.min = minutes
        self.sec = sec
    
    def input_time(self):
        self.hour = int(input("hour: "))
        self.min = int(input("minutes: "))
        self.sec = int(input("seconds: "))

    def __add__(self,other):

        totalsec = self.sec + other.sec
        totalmin = self.min + other.min +totalsec//60
        totalhrs = self.hour + other.hour + totalmin//60
        
        return time(totalhrs, totalmin%60, totalsec%60)
    
    def display(self):
        
        print(F"TIME: {self.hour} hours {self.min} minutes and {self.sec} seconds")
        
t1 = time()
t2 = time()
print("First Time")
t1.input_time()
print("\n\nSecond Time")
t2.input_time()

t3 = t1+t2
print("\n\nThe total time")
t3.display()