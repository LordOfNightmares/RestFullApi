def test(*args, **kwargs):
    print(args)
    print(kwargs)
test(1,2,3,help=1,no=2)