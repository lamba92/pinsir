import logging
import grpc
import tensorflow as tf

from concurrent import futures
import os
from embedder_app import EmbedderApp

from embedding_pb2_grpc import add_EmbeddingServicer_to_server

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_EmbeddingServicer_to_server(EmbedderApp(), server)
    server.add_insecure_port('[::]:'+os.environ["PORT"])
    logging.basicConfig()
    server.start()
    server.wait_for_termination()
