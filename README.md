# gRPC Python - Equisd client

## Ejecutar para re-generar los archivos pb2

python -m grpc_tools.protoc --proto_path=./protos equisd.proto --python_out=./generated/ --grpc_python_out=./generated/

## O mejor:

- python -m grpc_tools.protoc --python_out=. -I. protos/equisd.proto
- python -m grpc_tools.protoc --grpc_python_out=. -I. protos/equisd.proto
