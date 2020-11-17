# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import extraction_pb2 as extraction__pb2


class ExtractionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.extract = channel.unary_unary(
                '/Extraction/extract',
                request_serializer=extraction__pb2.ExtractionRequest.SerializeToString,
                response_deserializer=extraction__pb2.ExtractionResponse.FromString,
                )


class ExtractionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def extract(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExtractionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'extract': grpc.unary_unary_rpc_method_handler(
                    servicer.extract,
                    request_deserializer=extraction__pb2.ExtractionRequest.FromString,
                    response_serializer=extraction__pb2.ExtractionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Extraction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Extraction(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def extract(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Extraction/extract',
            extraction__pb2.ExtractionRequest.SerializeToString,
            extraction__pb2.ExtractionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)