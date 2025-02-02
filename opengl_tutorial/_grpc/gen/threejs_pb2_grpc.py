# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import threejs_pb2 as threejs__pb2


class TestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetHello = channel.unary_unary(
                '/testservice.TestService/GetHello',
                request_serializer=threejs__pb2.HelloRequest.SerializeToString,
                response_deserializer=threejs__pb2.HelloResponse.FromString,
                )


class TestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetHello': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHello,
                    request_deserializer=threejs__pb2.HelloRequest.FromString,
                    response_serializer=threejs__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'testservice.TestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.TestService/GetHello',
            threejs__pb2.HelloRequest.SerializeToString,
            threejs__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class GeometryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BoxGeometry = channel.unary_unary(
                '/testservice.GeometryService/BoxGeometry',
                request_serializer=threejs__pb2.BoxGeometryRequest.SerializeToString,
                response_deserializer=threejs__pb2.GeometryResponse.FromString,
                )
        self.SphereGeometry = channel.unary_unary(
                '/testservice.GeometryService/SphereGeometry',
                request_serializer=threejs__pb2.SphereGeometryRequest.SerializeToString,
                response_deserializer=threejs__pb2.GeometryResponse.FromString,
                )
        self.TorusKnotGeometry = channel.unary_unary(
                '/testservice.GeometryService/TorusKnotGeometry',
                request_serializer=threejs__pb2.TorusKnotGeometryRequest.SerializeToString,
                response_deserializer=threejs__pb2.GeometryResponse.FromString,
                )
        self.IcosahedronGeometry = channel.unary_unary(
                '/testservice.GeometryService/IcosahedronGeometry',
                request_serializer=threejs__pb2.IcosahedronGeometryRequest.SerializeToString,
                response_deserializer=threejs__pb2.GeometryResponse.FromString,
                )
        self.TetrahedronGeometry = channel.unary_unary(
                '/testservice.GeometryService/TetrahedronGeometry',
                request_serializer=threejs__pb2.TetrahedronGeometryRequest.SerializeToString,
                response_deserializer=threejs__pb2.GeometryResponse.FromString,
                )
        self.CylinderGeometry = channel.unary_unary(
                '/testservice.GeometryService/CylinderGeometry',
                request_serializer=threejs__pb2.CylinderGeometryRequest.SerializeToString,
                response_deserializer=threejs__pb2.GeometryResponse.FromString,
                )
        self.ConeGeometry = channel.unary_unary(
                '/testservice.GeometryService/ConeGeometry',
                request_serializer=threejs__pb2.ConeGeometryRequest.SerializeToString,
                response_deserializer=threejs__pb2.GeometryResponse.FromString,
                )
        self.CircleGeometry = channel.unary_unary(
                '/testservice.GeometryService/CircleGeometry',
                request_serializer=threejs__pb2.CircleGeometryRequest.SerializeToString,
                response_deserializer=threejs__pb2.GeometryResponse.FromString,
                )
        self.PlaneGeometry = channel.unary_unary(
                '/testservice.GeometryService/PlaneGeometry',
                request_serializer=threejs__pb2.PlaneGeometryRequest.SerializeToString,
                response_deserializer=threejs__pb2.GeometryResponse.FromString,
                )
        self.ExtrudeGeometry = channel.unary_unary(
                '/testservice.GeometryService/ExtrudeGeometry',
                request_serializer=threejs__pb2.ExtrudeGeometryRequest.SerializeToString,
                response_deserializer=threejs__pb2.GeometryResponse.FromString,
                )


class GeometryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BoxGeometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SphereGeometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TorusKnotGeometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IcosahedronGeometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TetrahedronGeometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CylinderGeometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConeGeometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CircleGeometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlaneGeometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExtrudeGeometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GeometryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BoxGeometry': grpc.unary_unary_rpc_method_handler(
                    servicer.BoxGeometry,
                    request_deserializer=threejs__pb2.BoxGeometryRequest.FromString,
                    response_serializer=threejs__pb2.GeometryResponse.SerializeToString,
            ),
            'SphereGeometry': grpc.unary_unary_rpc_method_handler(
                    servicer.SphereGeometry,
                    request_deserializer=threejs__pb2.SphereGeometryRequest.FromString,
                    response_serializer=threejs__pb2.GeometryResponse.SerializeToString,
            ),
            'TorusKnotGeometry': grpc.unary_unary_rpc_method_handler(
                    servicer.TorusKnotGeometry,
                    request_deserializer=threejs__pb2.TorusKnotGeometryRequest.FromString,
                    response_serializer=threejs__pb2.GeometryResponse.SerializeToString,
            ),
            'IcosahedronGeometry': grpc.unary_unary_rpc_method_handler(
                    servicer.IcosahedronGeometry,
                    request_deserializer=threejs__pb2.IcosahedronGeometryRequest.FromString,
                    response_serializer=threejs__pb2.GeometryResponse.SerializeToString,
            ),
            'TetrahedronGeometry': grpc.unary_unary_rpc_method_handler(
                    servicer.TetrahedronGeometry,
                    request_deserializer=threejs__pb2.TetrahedronGeometryRequest.FromString,
                    response_serializer=threejs__pb2.GeometryResponse.SerializeToString,
            ),
            'CylinderGeometry': grpc.unary_unary_rpc_method_handler(
                    servicer.CylinderGeometry,
                    request_deserializer=threejs__pb2.CylinderGeometryRequest.FromString,
                    response_serializer=threejs__pb2.GeometryResponse.SerializeToString,
            ),
            'ConeGeometry': grpc.unary_unary_rpc_method_handler(
                    servicer.ConeGeometry,
                    request_deserializer=threejs__pb2.ConeGeometryRequest.FromString,
                    response_serializer=threejs__pb2.GeometryResponse.SerializeToString,
            ),
            'CircleGeometry': grpc.unary_unary_rpc_method_handler(
                    servicer.CircleGeometry,
                    request_deserializer=threejs__pb2.CircleGeometryRequest.FromString,
                    response_serializer=threejs__pb2.GeometryResponse.SerializeToString,
            ),
            'PlaneGeometry': grpc.unary_unary_rpc_method_handler(
                    servicer.PlaneGeometry,
                    request_deserializer=threejs__pb2.PlaneGeometryRequest.FromString,
                    response_serializer=threejs__pb2.GeometryResponse.SerializeToString,
            ),
            'ExtrudeGeometry': grpc.unary_unary_rpc_method_handler(
                    servicer.ExtrudeGeometry,
                    request_deserializer=threejs__pb2.ExtrudeGeometryRequest.FromString,
                    response_serializer=threejs__pb2.GeometryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'testservice.GeometryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GeometryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BoxGeometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.GeometryService/BoxGeometry',
            threejs__pb2.BoxGeometryRequest.SerializeToString,
            threejs__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SphereGeometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.GeometryService/SphereGeometry',
            threejs__pb2.SphereGeometryRequest.SerializeToString,
            threejs__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TorusKnotGeometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.GeometryService/TorusKnotGeometry',
            threejs__pb2.TorusKnotGeometryRequest.SerializeToString,
            threejs__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IcosahedronGeometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.GeometryService/IcosahedronGeometry',
            threejs__pb2.IcosahedronGeometryRequest.SerializeToString,
            threejs__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TetrahedronGeometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.GeometryService/TetrahedronGeometry',
            threejs__pb2.TetrahedronGeometryRequest.SerializeToString,
            threejs__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CylinderGeometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.GeometryService/CylinderGeometry',
            threejs__pb2.CylinderGeometryRequest.SerializeToString,
            threejs__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConeGeometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.GeometryService/ConeGeometry',
            threejs__pb2.ConeGeometryRequest.SerializeToString,
            threejs__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CircleGeometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.GeometryService/CircleGeometry',
            threejs__pb2.CircleGeometryRequest.SerializeToString,
            threejs__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlaneGeometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.GeometryService/PlaneGeometry',
            threejs__pb2.PlaneGeometryRequest.SerializeToString,
            threejs__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExtrudeGeometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.GeometryService/ExtrudeGeometry',
            threejs__pb2.ExtrudeGeometryRequest.SerializeToString,
            threejs__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MaterialServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BasicMaterial = channel.unary_unary(
                '/testservice.MaterialService/BasicMaterial',
                request_serializer=threejs__pb2.BasicMaterialRequest.SerializeToString,
                response_deserializer=threejs__pb2.MaterialResponse.FromString,
                )
        self.PhongMaterial = channel.unary_unary(
                '/testservice.MaterialService/PhongMaterial',
                request_serializer=threejs__pb2.PhongMaterialRequest.SerializeToString,
                response_deserializer=threejs__pb2.MaterialResponse.FromString,
                )
        self.StandardMaterial = channel.unary_unary(
                '/testservice.MaterialService/StandardMaterial',
                request_serializer=threejs__pb2.StandardMaterialRequest.SerializeToString,
                response_deserializer=threejs__pb2.MaterialResponse.FromString,
                )


class MaterialServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BasicMaterial(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PhongMaterial(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StandardMaterial(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MaterialServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BasicMaterial': grpc.unary_unary_rpc_method_handler(
                    servicer.BasicMaterial,
                    request_deserializer=threejs__pb2.BasicMaterialRequest.FromString,
                    response_serializer=threejs__pb2.MaterialResponse.SerializeToString,
            ),
            'PhongMaterial': grpc.unary_unary_rpc_method_handler(
                    servicer.PhongMaterial,
                    request_deserializer=threejs__pb2.PhongMaterialRequest.FromString,
                    response_serializer=threejs__pb2.MaterialResponse.SerializeToString,
            ),
            'StandardMaterial': grpc.unary_unary_rpc_method_handler(
                    servicer.StandardMaterial,
                    request_deserializer=threejs__pb2.StandardMaterialRequest.FromString,
                    response_serializer=threejs__pb2.MaterialResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'testservice.MaterialService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MaterialService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BasicMaterial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.MaterialService/BasicMaterial',
            threejs__pb2.BasicMaterialRequest.SerializeToString,
            threejs__pb2.MaterialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PhongMaterial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.MaterialService/PhongMaterial',
            threejs__pb2.PhongMaterialRequest.SerializeToString,
            threejs__pb2.MaterialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StandardMaterial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/testservice.MaterialService/StandardMaterial',
            threejs__pb2.StandardMaterialRequest.SerializeToString,
            threejs__pb2.MaterialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
