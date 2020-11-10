import logging
from concurrent import futures
import os

import grpc

from detector_app import DetectorApp
from detection_pb2_grpc import add_DetectionServicer_to_server

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_DetectionServicer_to_server(DetectorApp(), server)
    server.add_insecure_port('[::]:' + os.environ['PORT'])
    logging.basicConfig()
    server.start()
    server.wait_for_termination()
