import logging
from concurrent import futures
import os

import grpc

from comparison_app import ComparisonApp
from comparison_pb2_grpc import add_ComparisonServicer_to_server

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ComparisonServicer_to_server(ComparisonApp(), server)
    server.add_insecure_port('[::]:' + os.environ['PORT'])
    logging.basicConfig()
    server.start()
    server.wait_for_termination()
