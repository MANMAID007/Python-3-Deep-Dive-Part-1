a = 100
print(id(a))
print(hex(id(a)))
a = "hello"
print(id(a))
print(hex(id(a)))
print("-------------------------------")

# reference counts
import sys, ctypes

l = [1, 2, 3]
k = l
print(l)
print(sys.getrefcount(l))


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


print(ref_count(id(l)))
a = 10
a_id = id(a)
a = None
print(ref_count(a_id))
print(ref_count(a_id))
print(ref_count(a_id))
print(ref_count(a_id))
print("-------------------------------")

# Garbage collection
import gc


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"


class A:
    def __init__(self):
        self.b = B(self)
        print("A: {}, b: {}".format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print("B: {}, a: {}".format(hex(id(self)), hex(id(self.a))))


gc.disable()

var1 = A()
print(hex(id(var1)))
# circular references
print(hex(id(var1.b)))
print(hex(id(var1.b.a)))

a_id = id(var1)
b_id = id(var1.b)

print("ref count of a: {}, ref count of b: {}".format(ref_count(a_id), ref_count(b_id)))

print("a {}, b {}".format(object_by_id(a_id), object_by_id(b_id)))

# deleting ref of var1
var1 = None
print("After removing the ref: a {}, b {}".format(object_by_id(a_id),
                                                  object_by_id(b_id)))  # we can see the ref are still exist

# Using GC collect
gc.collect()
print("After running gc.collect method: a {}, b {}".format(object_by_id(a_id),
                                                           object_by_id(b_id)))  # we can see the ref are removed
gc.enable()
print("-------------------------------")

# Dynamic typing
a = "hello"
print("a is {}, type of a: {}".format(a, type(a)))
a = 100
print("a is {}, type of a: {}".format(a, type(a)))
print("-------------------------------")

# Value Reassignment
a = 10
print("hex id when a is {}: {}".format(a, hex(id(a))))
a = 15
print("hex id when a is {}: {}".format(a, hex(id(a))))
b = 67
print("hex id when b is {}: {}".format(b, hex(id(b))))
b = b + 67
print("hex id when b is {}: {}".format(b, hex(id(b))))
c = 134
print("hex id when c is {}: {}".format(c, hex(id(c))))  # it is same as b(?)
print("-------------------------------")

# Object Mutability
t = ([1, 2], [1, 2, 3])
print("hex id of t with no change: {}".format(hex(id(t))))
print("hex id of t_0 with no change: {}".format(hex(id(t[0]))))
print("hex id of t_1 with no change: {}".format(hex(id(t[1]))))
t[0].append(3)
print("hex id of t with after change: {}".format(hex(id(t))))
print("hex id of t_0 with after change: {}".format(hex(id(t[0]))))
print("hex id of t_1 with after change: {}".format(hex(id(t[1]))))
print("-------------------------------")

# Shared References and Mutability
s1 = "hello"
s2 = s1
print("reference of s1 ({}) and s2 ({}) are: {}, {}".format(s1, s2, hex(id(s1)), hex(id(s2))))  # same
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print("reference of l1 ({}) and l2 ({}) are: {}, {}".format(l1, l2, hex(id(l1)), hex(id(l2))))  # not same since mutable
print("-------------------------------")


# Variable Equality
def equal_value(var_1, var_2):
    print("a is {}, b is {}. a is b {}, a == b {}".format(var_1, var_2, var_1 is var_2, var_1 == var_2))

equal_value(10, 10.0)
equal_value(1500012345, 1500012345)
equal_value(None, None)
equal_value([1, 2, 3], [1, 2, 3])
print("-------------------------------")

# Everything is Object
print(type(type(type)))
print(type(help))
print("-------------------------------")

# String Interning
a = "hello-gg"
b = "hello-gg"
equal_value(a, b)
a = "hello gg"
b = "hello gg"
equal_value(a, b)
a = sys.intern("hello gg")
b = sys.intern("hello gg")
equal_value(a, b)
print("---------------END----------------")



