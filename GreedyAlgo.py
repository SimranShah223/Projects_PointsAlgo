from time import time


class Greedy:
    def __init__(self, QualityRating, FundingRequest):
        self.FundingRequest = FundingRequest
        self.QualityRating = QualityRating


def GreedyAlgo(TotalFunds, FundingArray, LengthList):
    if TotalFunds <= 0:
        return 0
    FundingArray.sort(key=lambda GAlgo: GAlgo.QualityRating / GAlgo.FundingRequest if GAlgo.FundingRequest > 0 else 1,
                      reverse=True)
    SumQualityParameter = 0
    count = 0
    while count < LengthList:
        if FundingArray[count].FundingRequest <= TotalFunds:
            TotalFunds = TotalFunds - FundingArray[count].FundingRequest
            SumQualityParameter = SumQualityParameter + FundingArray[count].QualityRating
        count += 1
    return SumQualityParameter


if __name__ == '__main__':
    init = time()
    TotalFunds = 10000
    FundingArray = [Greedy(1000, 1000), Greedy(500, 2000), Greedy(800, 4000), Greedy(500, 3000), Greedy(120, 1500),
                    Greedy(400, 5000), Greedy(300, 5000)]
    LengthList = len(FundingArray)
    print("Maximum Quantity: " + str(GreedyAlgo(TotalFunds, FundingArray, LengthList)) + " and Run time = " + str(time() - init))

    init = time()
    TotalFunds = 60
    FundingArray = [Greedy(10, 1), Greedy(50, 2), Greedy(80, 4), Greedy(50, 3), Greedy(12, 15),
                    Greedy(40, 5), Greedy(30, 5), Greedy(40, 1), Greedy(20, 1), Greedy(100, 2),
                    Greedy(1001, 2), Greedy(200, 3), Greedy(2, 2), Greedy(1, 1)]
    LengthList = len(FundingArray)
    print("Maximum Quantity: " + str(GreedyAlgo(TotalFunds, FundingArray, LengthList)) + " and Run time = " + str(time() - init))

    init = time()
    TotalFunds = 60
    FundingArray = [Greedy(1, 0), Greedy(3, 2), Greedy(0, 4), Greedy(500, 3), Greedy(120, 15),
                    Greedy(2000, 2), Greedy(3000, 3), Greedy(4000, 4), Greedy(5000, 5), Greedy(6000, 6),
                    Greedy(7000, 7), Greedy(8000, 8), Greedy(9000, 9), Greedy(1000, 1), Greedy(2000, 2)]
    LengthList = len(FundingArray)
    print("Maximum Quantity: " + str(GreedyAlgo(TotalFunds, FundingArray, LengthList)) + " and Run time = " + str(time() - init))

    init = time()
    TotalFunds = -100
    FundingArray = [Greedy(50, 100), Greedy(60, 200), Greedy(7009, 400), Greedy(54500, 300), Greedy(13420, 150),
                    Greedy(43400, 500), Greedy(33400, 500)]
    LengthList = len(FundingArray)
    print("Maximum Quantity: " + str(GreedyAlgo(TotalFunds, FundingArray, LengthList)) + " and Run time = " + str(time() - init))

    init = time()
    TotalFunds = 2
    FundingArray = [Greedy(323, 10), Greedy(554, 2), Greedy(434, 10)]
    LengthList = len(FundingArray)
    print("Maximum Quantity: " + str(GreedyAlgo(TotalFunds, FundingArray, LengthList)) + " and Run time = " + str(time() - init))

