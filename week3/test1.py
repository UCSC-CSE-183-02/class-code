
routes = {}

def a(f):
    def g():
        r = f()
        return r + 'a'    
    return g

def b(f):
    def g():
        r = f()
        return r + 'b'    
    return g

def c(f):
    def g():
        r = f()
        return r + 'c'    
    return g

def f():
    return "x"

f = a(b(c(f)))

print(f())