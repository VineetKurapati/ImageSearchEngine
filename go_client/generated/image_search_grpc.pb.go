// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v4.25.3
// source: image_search.proto

package generated

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

const (
	ImageSearch_SearchImage_FullMethodName = "/image_search.ImageSearch/SearchImage"
	ImageSearch_Ping_FullMethodName        = "/image_search.ImageSearch/Ping"
)

// ImageSearchClient is the client API for ImageSearch service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ImageSearchClient interface {
	SearchImage(ctx context.Context, in *SearchRequest, opts ...grpc.CallOption) (*ImageResponse, error)
	Ping(ctx context.Context, in *PingRequest, opts ...grpc.CallOption) (*PingResponse, error)
}

type imageSearchClient struct {
	cc grpc.ClientConnInterface
}

func NewImageSearchClient(cc grpc.ClientConnInterface) ImageSearchClient {
	return &imageSearchClient{cc}
}

func (c *imageSearchClient) SearchImage(ctx context.Context, in *SearchRequest, opts ...grpc.CallOption) (*ImageResponse, error) {
	out := new(ImageResponse)
	err := c.cc.Invoke(ctx, ImageSearch_SearchImage_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *imageSearchClient) Ping(ctx context.Context, in *PingRequest, opts ...grpc.CallOption) (*PingResponse, error) {
	out := new(PingResponse)
	err := c.cc.Invoke(ctx, ImageSearch_Ping_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ImageSearchServer is the server API for ImageSearch service.
// All implementations must embed UnimplementedImageSearchServer
// for forward compatibility
type ImageSearchServer interface {
	SearchImage(context.Context, *SearchRequest) (*ImageResponse, error)
	Ping(context.Context, *PingRequest) (*PingResponse, error)
	mustEmbedUnimplementedImageSearchServer()
}

// UnimplementedImageSearchServer must be embedded to have forward compatible implementations.
type UnimplementedImageSearchServer struct {
}

func (UnimplementedImageSearchServer) SearchImage(context.Context, *SearchRequest) (*ImageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SearchImage not implemented")
}
func (UnimplementedImageSearchServer) Ping(context.Context, *PingRequest) (*PingResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Ping not implemented")
}
func (UnimplementedImageSearchServer) mustEmbedUnimplementedImageSearchServer() {}

// UnsafeImageSearchServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ImageSearchServer will
// result in compilation errors.
type UnsafeImageSearchServer interface {
	mustEmbedUnimplementedImageSearchServer()
}

func RegisterImageSearchServer(s grpc.ServiceRegistrar, srv ImageSearchServer) {
	s.RegisterService(&ImageSearch_ServiceDesc, srv)
}

func _ImageSearch_SearchImage_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SearchRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ImageSearchServer).SearchImage(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ImageSearch_SearchImage_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ImageSearchServer).SearchImage(ctx, req.(*SearchRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ImageSearch_Ping_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PingRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ImageSearchServer).Ping(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ImageSearch_Ping_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ImageSearchServer).Ping(ctx, req.(*PingRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// ImageSearch_ServiceDesc is the grpc.ServiceDesc for ImageSearch service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ImageSearch_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "image_search.ImageSearch",
	HandlerType: (*ImageSearchServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "SearchImage",
			Handler:    _ImageSearch_SearchImage_Handler,
		},
		{
			MethodName: "Ping",
			Handler:    _ImageSearch_Ping_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "image_search.proto",
}