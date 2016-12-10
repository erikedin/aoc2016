class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def is_possible(self):
        return (
            self.s1 + self.s2 > self.s3 and 
            self.s1 + self.s3 > self.s2 and 
            self.s2 + self.s3 > self.s1) 

class TriangleCounter:
    def __init__(self, triangles):
        self.triangles = triangles
    
    def possibles(self):
        return filter(lambda x: x.is_possible(), self.triangles)