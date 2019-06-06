def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            def helper():
                print(i)
            return helper
        print(print_i())
        flist.append(print_i())

    return flist

functions = make_functions()
for f in functions:
    f()
