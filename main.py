import grpc
from concurrent import futures
import time
import protos.equisd_pb2_grpc as pb2_grpc
import protos.equisd_pb2 as pb2


class EquisDeServiceImpl(pb2_grpc.EquisDeServicer):

    def __init__(self, *args, **kwargs):
        pass

    def Ping(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'Hello I am up and running received "{message}" message from you'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)
def serve():
    import os
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_EquisDeServicer_to_server(EquisDeServiceImpl(), server)
    port = int(os.environ.get('PORT', '50051'))  # Default to 50051 if not set
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"Running at {port}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()