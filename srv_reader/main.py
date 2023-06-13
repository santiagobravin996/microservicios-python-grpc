import sales_records_pb2
import sales_records_pb2_grpc
import grpc
import os 

from repositories.file_repository import FileRepository


def main(): 
    
    file_repository = FileRepository("/tmp/data/10000_sr.csv")
    
    data_readed = file_repository.read_data()
    
    source = os.environ['HOSTNAME']
    
    for row in data_readed:
        with grpc.insecure_channel("srv_persistor:50051") as channel:
            stub = sales_records_pb2_grpc.SalesRecordStub(channel) #nos va a decir a que servicio dentro del servidor nos vamos a conectar.
            request = sales_records_pb2.SalesRecordsRequest(region=row[0], item_type=row[1],units_sold=row[2],unit_price=row[3], unit_cost=row[4],source = source)
            response = stub.SendSalesRecord(request)                            
            print(f"gRPC received: {response.data}")
        
        
if __name__ == "__main__": 
    main()
    