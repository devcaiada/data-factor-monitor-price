from azure.storage.blob import BlobServiceClient

# Configuração
connect_str = "<SUA_CONNECTION_STRING>"
container_name = "meu-container"
blob_name = "meu-arquivo.txt"
file_path = "./meu-arquivo.txt"

# Criar o cliente do serviço Blob
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Upload do arquivo
with open(file_path, "rb") as data:
    blob_client.upload_blob(data)

print(f"Arquivo {blob_name} enviado com sucesso!")