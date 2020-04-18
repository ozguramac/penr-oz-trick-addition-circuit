def foo(l):
    al = []
    c = 1
    for d in reversed(l):
        ad = (d + c)
        al.insert(0, (ad % 10))
        c = ad // 10
    if c > 0:
        al.insert(0, c)

    return al


def test(l, eal):
    al = foo(l)
    print("{} => {}".format(l, al))
    assert eal == al


test([0], [1])
test([5], [6])
test([9], [1, 0])
test([6, 6], [6, 7])
test([8, 9], [9, 0])
test([9, 9], [1, 0 ,0])