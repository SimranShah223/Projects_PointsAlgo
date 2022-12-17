from time import time


def DynamicAlgo(FundingRequest, QualityRating, LengthList, TotalFunds):
    if ListLen <= 0 or TotalFunds <= 0:
        return 0
    Table = [[0 for x in range(0, TotalFunds + 1)]
             for x in range(0, LengthList + 1)]

    for x in range(0, LengthList + 1):
        for z in range(0, TotalFunds + 1):
            if x <= 0 or z <= 0:
                Table[x][z] = 0
            elif FundingRequest[x - 1] <= z:
                Table[x][z] = max(QualityRating[x - 1]
                              + Table[x - 1][z - FundingRequest[x - 1]],
                              Table[x - 1][z])
            else:
                Table[x][z] = Table[x - 1][z]

    return Table[LengthList][TotalFunds]


if __name__  == '__main__':
    init = time()
    QualityRating = [1000, 500, 800, 500, 120, 400, 300]
    FundingRequest = [1000, 2000, 4000, 3000, 1500, 5000, 5000]
    TotalFunds = 10000
    ListLen = len(QualityRating)
    print("Maximum Quantity: " + str(DynamicAlgo(FundingRequest, QualityRating, ListLen, TotalFunds)) + " and Run time "
                                                                                                        "= " + str(
        time()
        - init))

    init = time()
    QualityRating = [10, 50, 80, 50, 12, 40, 30, 40, 20, 100, 1001, 200, 2, 1]
    FundingRequest = [1, 2, 4, 3, 15, 5, 5, 1, 1, 2, 2, 3, 2, 1]
    TotalFunds = 60
    ListLen = len(QualityRating)
    print("Maximum Quantity: " + str(DynamicAlgo(FundingRequest, QualityRating, ListLen, TotalFunds)) + " and Run time "
                                                                                                        "= " + str(
        time()
        - init))

    init = time()
    QualityRating = [1, 3, 0, 500, 120, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 1000, 2000]
    FundingRequest = [0, 2, 4, 3, 15, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]
    TotalFunds = 60
    ListLen = len(QualityRating)
    print("Maximum Quantity: " + str(DynamicAlgo(FundingRequest, QualityRating, ListLen, TotalFunds)) + " and Run time "
                                                                                                        "= " + str(
        time()
        - init))

    init = time()
    QualityRating = [50, 60, 7009, 54500, 13420, 43400, 33400]
    FundingRequest = [100, 200, 400, 300, 150, 500, 500]
    TotalFunds = -100
    ListLen = len(QualityRating)
    print("Maximum Quantity: " + str(DynamicAlgo(FundingRequest, QualityRating, ListLen, TotalFunds)) + " and Run time "
                                                                                                        "= " + str(
        time()
        - init))
    init = time()
    QualityRating = [323, 554, 434]
    FundingRequest = [10, 2, 10]
    TotalFunds = 2
    ListLen = len(QualityRating)
    print("Maximum Quantity: " + str(DynamicAlgo(FundingRequest, QualityRating, ListLen, TotalFunds)) + " and Run time "
                                                                                                        "= " + str(
        time()
        - init))


