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
                l.append(i)
        self.data = l
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
            print("no elem")

    
#issubset
a = Set([1,2,3,4])
b = Set([1,2])
print(b.issubset(a))
#issuperset
print(b.issuperset(a))
print(a.issuperset(b))

x = Set([1,3,5,7, 1, 3])
y = Set([2,1,4,5,6])
z = Set([5,6,7,8,9])
print(x, y, len(x))
#intersection_update
# 세트를 업데이트하고 그 세트에서 발견 된 요소 만 유지합니다.
# print(x.intersection_update(y,z))
#difference_update
#세트를 업데이트하고 다른 세트에서 발견 된 요소를 제거합니다.
# print(x.difference_update(y,z))
#symmetric_difference_update(other)
print(a.symmetric_difference_update(b))
print(a, b)
# 세트에서 업데이트 된 요소 만 유지하고 두 세트 모두에서 요소는 유지하지 않습니다.
#add(elem)
# 세트에 요소 elem 을 추가하십시오 .
a.add(5)
print(a)
#remove(elem)remove(elem)
#세트에서 요소 elem 을 제거하십시오 . 발생시킵니다 KeyError경우 ELEM이 세트에 포함되어 있지 않습니다.
print(x, y, len(x))
print(x.intersection(y), y.union(x))
print(x & y, x | y)
# print(x[2], y[:2])
for element in x:
    print(element, end=' ')
print()
print(3 not in y)  # membership test
print(list(x))   # convert to list because x is iterable