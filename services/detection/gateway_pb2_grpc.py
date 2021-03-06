# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import common_pb2 as common__pb2
import gateway_pb2 as gateway__pb2


class GatewayStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.elaborate = channel.unary_unary(
                '/Gateway/elaborate',
                request_serializer=gateway__pb2.ElaborationRequest.SerializeToString,
                response_deserializer=gateway__pb2.ElaborationResponse.FromString,
                )
        self.comparePortraits = channel.unary_unary(
                '/Gateway/comparePortraits',
                request_serializer=gateway__pb2.ComparePortraitsRequest.SerializeToString,
                response_deserializer=common__pb2.ComparisonResult.FromString,
                )
        self.comparePortraitToGallery = channel.unary_unary(
                '/Gateway/comparePortraitToGallery',
                request_serializer=gateway__pb2.ComparePortraitToGalleryRequest.SerializeToString,
                response_deserializer=common__pb2.ComparisonResponse.FromString,
                )


class GatewayServicer(object):
    """Missing associated documentation comment in .proto file."""

    def elaborate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def comparePortraits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def comparePortraitToGallery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GatewayServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'elaborate': grpc.unary_unary_rpc_method_handler(
                    servicer.elaborate,
                    request_deserializer=gateway__pb2.ElaborationRequest.FromString,
                    response_serializer=gateway__pb2.ElaborationResponse.SerializeToString,
            ),
            'comparePortraits': grpc.unary_unary_rpc_method_handler(
                    servicer.comparePortraits,
                    request_deserializer=gateway__pb2.ComparePortraitsRequest.FromString,
                    response_serializer=common__pb2.ComparisonResult.SerializeToString,
            ),
            'comparePortraitToGallery': grpc.unary_unary_rpc_method_handler(
                    servicer.comparePortraitToGallery,
                    request_deserializer=gateway__pb2.ComparePortraitToGalleryRequest.FromString,
                    response_serializer=common__pb2.ComparisonResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Gateway', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Gateway(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def elaborate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Gateway/elaborate',
            gateway__pb2.ElaborationRequest.SerializeToString,
            gateway__pb2.ElaborationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def comparePortraits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Gateway/comparePortraits',
            gateway__pb2.ComparePortraitsRequest.SerializeToString,
            common__pb2.ComparisonResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def comparePortraitToGallery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Gateway/comparePortraitToGallery',
            gateway__pb2.ComparePortraitToGalleryRequest.SerializeToString,
            common__pb2.ComparisonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
