import grpc

from tushare_pb2 import *
from util import *
import tushare_pb2_grpc
import tushare as ts
from concurrent import futures
import logging

class TushareService(tushare_pb2_grpc.TushareServiceServicer):
    def MoneySupply(self, request, context):
        df = ts.get_money_supply()
        return result(df)

    def HistData(self, request, context):
        code = request.code
        start = date_to_str(request.start)
        end = date_to_str(request.end)
        ktype = ktype_to_str(request.kType)
        df = ts.get_hist_data(code, start, end, ktype)
        return result(df)

    def TickData(self, request, context):
        code = request.code
        date = date_to_str(request.date)
        df = ts.get_tick_data(code, date)
        return result(df)

    def StockBasics(self, request, context):
        df = ts.get_stock_basics()
        return result(df)

    def TodayAll(self, request, context):
        df = ts.get_today_all()
        return result(df)

    def TodayTicks(self, request, context):
        code = request.code
        df = ts.get_today_ticks(code)
        return result(df)
    def Index(self, request, context):
        df = ts.get_index()
        return result(df)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tushare_pb2_grpc.add_TushareServiceServicer_to_server(
        TushareService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()