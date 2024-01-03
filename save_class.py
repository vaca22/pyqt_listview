
class Order:
    def __init__(self, orderId, createTime, status, goodsName, productCnt, total_address, nextKey, bizuin,totalPage,totalNum):
        self.orderId = orderId
        self.createTime = createTime
        self.status = status
        self.goodsName = goodsName
        self.productCnt = productCnt
        self.total_address = total_address
        self.nextKey = nextKey
        self.bizuin = bizuin
        self.totalPage = totalPage
        self.totalNum = totalNum
