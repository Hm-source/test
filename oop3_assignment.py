class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:
    
    def issubset(self, other) :
        count = 0
        for i in self.data :
            if i in other.data :
                count += 1            
            if count == len(self.data) :
                return True
        else :
            return False

    def issuperset(self, other) :
        count = 0
        for i in other.data :
            if i in self.data:
                count += 1
        if count == len(other.data) :
            return True
        else :
            return False

    def intersection_update(self, *others) :
        x = self.data
        for i in others :
            for j in x :
                if j not in i :
                    x.remove(j)
        self = Set(x)
        return self


    def difference_update(self, *others) :
        a = self.data
        for i in others :
            for j in a :
                if j in i :
                    a.remove(j)
        self = Set(a)
        return self

    def symmetric_difference_update(self, other) :
        a = self.intersection(other)
        l = []
        for i in self.data :
            if i not in a.data :
                l.append(i)
        for j in other.data :
            if j not in a.data :
                l.append(j)
        self = Set(l)
        return self

    def add(self, elem) :
        if elem not in self.data :
            self.data.append(elem)
        
    def remove(self,elem) :
        try : 
            if elem in self.data :
                self.data.remove(elem)
            else :
                raise KeyError
        except KeyError : 
            print(f'There is no {elem}')

    def __lt__(self, other) :
        if self.data != other.data :
            return self.issubset(other)
        else : 
            return False
    
    def __le__(self, other) :
        return self.issubset(other)

    def __gt__(self, other) :
        if self.data != other.data :
            return self.issuperset(other)
        else :
            return False
    
    def __ge__(self, other) :
        return self.issuperset(other)
    
    def __ior__(self, other) :
        for i in other.data :
            if i not in self.data :
                self.data.append(i)
        return self

    def __ixor__(self, other) :
        new = []
        first = self.intersection(other)
        for i in self.data :
            if i not in first.data :
                new.append(i)
        for i in other.data :
            if i not in first.data :
                new.append(i)
        self = Set(new)
        return self

    def __iand__(self, other) :
        new = []
        a = self.intersection(other)
        new = a.data
        self = Set(new)
        return self

    def __isub__(self, other) :
        l = []
        a = self.intersection(other)
        for i in self.data :
            if i not in a.data :
                l.append(i)
        self = Set(l)
        return self

A = Set([1,2,3,4,5])
B = Set([2,3,4,7,8])
A^=B
print(A)

C = Set([1,2,3,4,5])
D = Set([3,4,5])
C&=D
print(C)

E = Set([1,2,3,5,6])
F = Set([7,4,3,5])
E|=F
print(E)

G = Set([2,5,6,9])
H = Set([3,5,7,9])
G-=H
print(G)

a = Set([1,2,3,4])
b = Set([1,2])  
print(a>=b)
print(a>b)
print(b<a)

#issubset
print(b.issubset(a))

#issuperset
print(b.issuperset(a))
print(a.issuperset(b))

aa = Set([1,2,3])
bb = Set([1,2,3])
print(aa>bb)
print(aa<bb)
print(aa.issubset(bb))
print(bb.issubset(aa))

x = Set([1,3,5,7, 1, 3])
y = Set([2,1,4,5,6])
z = Set([5,6,7,8,9])
print(x, y, z, len(x))

#intersection_update
print(x.intersection_update(y,z))
print(x, y, z, len(x))

#difference_update
d = Set([5,6,7,9])
e = Set([3,5,7,8,6])
f = Set([2,4,6,8])
print(d, e, f, len(d))
print(d.difference_update(e,f))
print(d, e, f, len(x))

#symmetric_difference_update(other)
my = Set([4,6,8,9])
your = Set([4,6,8,10])
print(my.symmetric_difference_update(your))
print(my)

#add(elem)
my1 = Set([4,6,7,8,9])
my1.add(8)
my1.add(19)
print(my1)

#remove(elem)remove(elem)
my2 = Set([3,6,8,9,11])
my2.remove(3)
my2.remove(2)
print(my2)