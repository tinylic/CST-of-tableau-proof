

class CST :

    def __invert__(self) :
        return Not(self)

    def __and__(self, other) :
        return And(self, other)

    def __or__(self, other) :
        return Or(self, other)

    def __rshift__(self, other) :
        return Imply(self, other)

    def __lshift__(self, other) :
        return Iff(self, other)

    def __eq__(self, other) :
        return self.__class__ == other.__class__ and self.eq(other)

    def _proof(self, left, right) :
        while True :
            found = True
            for item in left :
                print "T" + str(item)
                if item in right :
                    return None
                if not isinstance(item, Atom) :
                    left.remove(item)
                    tuples = item._tleft(left, right)
                    left, right = tuples[0]
                    if len(tuples) > 1 :
                        v = self._proof(*tuples[1])
                        if v is not None:
                            return v
                    found = False
                    break
            for item in right :
                print "F" + str(item)
                if item in left :
                    return None
                if not isinstance(item, Atom) :
                    right.remove(item)
                    tuples = item._tright(left, right)
                    left, right = tuples[0]
                    if len(tuples) > 1 :
                        v = self._proof(*tuples[1])
                        if v is not None:
                            return v
                    found = False
                    break
            if found :
                return set(left)

    def proof(self) :
        print "proof"
        print "F" + str(self)
        return self._proof([], [self])

class Atom(CST) :
    def __init__(self, name) :
        self.name = name

    def __hash__(self) :
        return hash(self.name)

    def v(self, v) :
        return self in v

    def __str__(self) :
        return str(self.name)

    __repr__ = __str__

    def eq(self, other) :
        return self.name == other.name

class Not(CST) :
    def __init__(self, child) :
        self.child = child

    def v(self, v) :
        return not self.child.v(v)

    def __str__(self) :
        return "\\not " + str(self.child)

    def eq(self, other) :
        return self.child == other.child

    def _tleft(self, left, right) :
        return (left, right + [self.child]),

    def _tright(self, left, right) :
        return (left + [self.child], right),

class BinOp(CST) :
    def __init__(self, lchild, rchild) :
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self) :
        return '(' + str(self.lchild) + " " + self.op + " " + str(self.rchild) + ")"

    def eq(self, other) :
        return self.lchild == other.lchild and self.rchild == other.rchild

class And(BinOp) :

    op = "\\and"

    def v(self, v) :
        return self.lchild.v(v) and self.rchild.v(v)

    def _tleft(self, left, right) :
        return (left + [self.lchild, self.rchild], right),

    def _tright(self, left, right) :
        return (left, right + [self.lchild]), (left, right + [self.rchild])

class Or(BinOp) :

    op = "\\or"

    def v(self, v) :
        return self.lchild.v(v) or self.rchild.v(v)

    def _tleft(self, left, right) :
        return (left + [self.lchild], right), (left + [self.rchild], right)

    def _tright(self, left, right) :
        return (left, right + [self.lchild, self.rchild]),

class Imply(BinOp) :

    op = "\\imply"

    def v(self, v) :
        return not self.lchild.v(v) or self.rchild.v(v)

    def _tleft(self, left, right) :
        return (left + [self.rchild], right), (left, right + [self.lchild])

    def _tright(self, left, right) :
        return (left + [self.lchild], right + [self.rchild]),

class Iff(BinOp) :

    op = "\\iff"

    def v(self, v) :
        return self.lchild.v(v) is self.rchild.v(v)

    def _tleft(self, left, right) :
        return (left + [self.lchild, self.rchild], right), (left, right + [self.lchild, self.lchild])

    def _tright(self, left, right) :
        return (left + [self.lchild], right + [self.rchild]), (left + [self.rchild], right + [self.lchild])
