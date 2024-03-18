# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import image_search_pb2 as image__search__pb2


class ImageSearchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchImage = channel.unary_unary(
                '/image_search.ImageSearch/SearchImage',
                request_serializer=image__search__pb2.SearchRequest.SerializeToString,
                response_deserializer=image__search__pb2.ImageResponse.FromString,
                )
        self.Ping = channel.unary_unary(
                '/image_search.ImageSearch/Ping',
                request_serializer=image__search__pb2.PingRequest.SerializeToString,
                response_deserializer=image__search__pb2.PingResponse.FromString,
                )


class ImageSearchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SearchImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageSearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SearchImage': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchImage,
                    request_deserializer=image__search__pb2.SearchRequest.FromString,
                    response_serializer=image__search__pb2.ImageResponse.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=image__search__pb2.PingRequest.FromString,
                    response_serializer=image__search__pb2.PingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'image_search.ImageSearch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageSearch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SearchImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/image_search.ImageSearch/SearchImage',
            image__search__pb2.SearchRequest.SerializeToString,
            image__search__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/image_search.ImageSearch/Ping',
            image__search__pb2.PingRequest.SerializeToString,
            image__search__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
