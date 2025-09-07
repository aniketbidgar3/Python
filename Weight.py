class Weight:
    def __init__(self,kg,gm):
        self.kg=kg
        self.gm=gm
    
    def __str__(self):
        return (f"{self.kg} kg, {self.gm} gm")



w1=Weight(76,500)
print(w1)