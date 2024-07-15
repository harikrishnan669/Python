def check_scope():
    def do_local():
        test="Local test"
    def do_nonlocal():
        nonlocal test
        test="Non local test"
    def do_global():
        test="Global test"
        
    test="default"
    do_local()
    print("The test value is:" + test)
    do_nonlocal()
    print("The test value is:"+ test)

check_scope()
