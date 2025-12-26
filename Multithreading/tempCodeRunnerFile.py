    with ProcessPoolExecutor(max_workers=20) as exe:
        res = exe.map(findNumberOfPrimes,numbers)

    for r in res:
        print(r)