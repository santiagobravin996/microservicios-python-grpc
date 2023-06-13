import grpc
import sales_records_pb2
import sales_records_pb2_grpc

from concurrent import futures


class SalesRecord(sales_records_pb2_grpc.SalesRecordServicer):
    def PingSalesRecord(self, request, context):
        response = sales_records_pb2.PingSalesRecordResponse(ack='1')
        return response

    def SendSalesRecord(self, request, context):
        print(request.region)
        print(request.source)
        response = sales_records_pb2.SalesRecordsRespose(data=request.unit_cost)
        return response
    
    
    
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sales_records_pb2_grpc.add_SalesRecordServicer_to_server(SalesRecord(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("servidor levantado con grpc")
    
    
    server.wait_for_termination() #garantizamos que nuestro servicio esté siempre escuchando




if __name__ == "__main__":
    main()