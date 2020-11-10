# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import detection_pb2 as detection__pb2


class DetectionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.detect = channel.unary_unary(
                '/Detection/detect',
                request_serializer=detection__pb2.DetectionRequest.SerializeToString,
                response_deserializer=detection__pb2.DetectionResponse.FromString,
                )


class DetectionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def detect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DetectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'detect': grpc.unary_unary_rpc_method_handler(
                    servicer.detect,
                    request_deserializer=detection__pb2.DetectionRequest.FromString,
                    response_serializer=detection__pb2.DetectionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Detection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Detection(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def detect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Detection/detect',
            detection__pb2.DetectionRequest.SerializeToString,
            detection__pb2.DetectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
