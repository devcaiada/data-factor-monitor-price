# 📊 Criando um Monitoramento de Custos no Data Factory

## 🚀 Visão Geral

Este projeto apresenta uma abordagem prática para explorar o ambiente **Azure** utilizando uma conta gratuita de estudante. O objetivo principal é **configurar o Azure Data Factory e monitorar o uso e os custos dos recursos implantados**. Durante a implementação, abordaremos os seguintes temas:

- ✔️ Estruturação de assinaturas e grupos de recursos.
- ✔️ Boas práticas de nomenclatura para facilitar a organização.
- ✔️ Personalização de dashboards para acompanhamento visual.
- ✔️ Utilização de métricas e alertas de custo para controle eficiente.
- ✔️ Automação com **ARM Templates** e **Azure Cloud Shell**.
- ✔️ Passo a passo completo para monitorar os gastos na plataforma.
- ✔️ Implementação de um **script Python** para automação do monitoramento de custos.

---

## 🛠️ Tecnologias Utilizadas

- **Azure Data Factory** 🌐
- **Azure Monitor** 📊
- **Azure Cost Management** 💰
- **Azure Cloud Shell** 🖥️
- **ARM Templates** 📄
- **Python + Azure SDK** 🐍

---

## 📌 Pré-requisitos

Antes de iniciar, certifique-se de ter:

- 🔹 Uma conta gratuita no **Azure for Students** ou **Azure Free Tier**.
- 🔹 Acesso ao **Azure Portal**.
- 🔹 Familiaridade com o **Azure Resource Manager (ARM)**.
- 🔹 Conhecimentos básicos em **PowerShell**, **CLI do Azure** e **Python**.

---

## 🏗 Passo a Passo da Implementação

### 1️⃣ Criando o Ambiente no Azure

1. Acesse o portal [Azure Portal](https://portal.azure.com/).
2. Crie um **Grupo de Recursos** para organizar os ativos.
3. Configure uma **Assinatura** vinculada à conta gratuita.
4. Defina um **Plano de Nomenclatura** para manter a padronização.

### 2️⃣ Implantando o Azure Data Factory

1. No **Azure Portal**, vá até "Criar um recurso" e selecione **Data Factory**.
2. Escolha o grupo de recursos criado anteriormente.
3. Defina a região e nome do serviço seguindo as boas práticas.
4. Conclua a implantação e acesse o painel do **Data Factory**.

### 3️⃣ Monitorando os Custos

1. Acesse **Azure Cost Management + Billing** no portal.
2. Configure **métricas de uso e custo** para o Data Factory.
3. Defina **alertas de custo** para evitar gastos inesperados.
4. Crie um **dashboard personalizado** para visualização simplificada.

### 4️⃣ Automação com Azure Cloud Shell

1. Acesse o **Azure Cloud Shell** no portal.
2. Utilize **PowerShell** ou **Azure CLI** para gerenciar recursos.
3. Automatize tarefas recorrentes com **scripts ARM Templates**.
4. Teste a criação e remoção automatizada de recursos para otimização.

### 5️⃣ Implementação com Python 🚀

Podemos automatizar o monitoramento dos custos do **Azure Data Factory** utilizando Python e a **Azure SDK**. Siga os passos abaixo:

#### 📌 Instale as bibliotecas necessárias:
```sh
pip install azure-identity azure-mgmt-costmanagement
```

#### 📝 Código em Python para Monitoramento de Custos:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient
import datetime


SUBSCRIPTION_ID = "xxxx-xxxx-xxxx-xxxx"
BUDGET_LIMIT = 50


credential = DefaultAzureCredential()
client = CostManagementClient(credential)

# Define o período para consulta (últimos 30 dias)
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=30)

# Consulta os custos do Data Factory
cost_request = {
    "type": "Usage",
    "timeframe": "Custom",
    "time_period": {
        "from": start_date.strftime('%Y-%m-%d'),
        "to": end_date.strftime('%Y-%m-%d')
    },
    "dataset": {
        "granularity": "Daily",
        "aggregation": {
            "totalCost": {
                "name": "PreTaxCost",
                "function": "Sum"
            }
        }
    }
}


response = client.query.usage(f"/subscriptions/{SUBSCRIPTION_ID}", cost_request)
total_cost = sum(item["totalCost"] for item in response.rows)

print(f"💰 Custo total nos últimos 30 dias: ${total_cost:.2f}")


# Verifica se o custo ultrapassou o limite
if total_cost > BUDGET_LIMIT:
    print("⚠️ ALERTA: O custo ultrapassou o limite definido!")
else:
    print("✅ Tudo certo! O custo está dentro do orçamento.")
```

Esse script **autentica no Azure**, **consulta os custos do Data Factory** e **gera alertas caso os gastos ultrapassem o limite definido**. 🚀

---

## 🎯 Resultados Esperados

- ✅ Melhor controle dos custos no Azure 💰.
- ✅ Configuração eficiente do **Data Factory** 🏗.
- ✅ Dashboards intuitivos para acompanhamento 📊.
- ✅ Automação e infraestrutura como código 📜.
- ✅ Monitoramento automatizado via **Python** 🤖.

---

## 📢 Contribuições

Sinta-se à vontade para contribuir! Sugestões, melhorias e feedbacks são bem-vindos.

📩 Para dúvidas ou sugestões, [entre em contato](https://www.linkedin.com/in/devcaiada)!

> 🚀 **Vamos juntos monitorar e otimizar nosso uso no Azure!** 💙
----
<br></br>
<br></br>

# 🛠 Redundância de Arquivos no Azure com Data Factory

## ✨ Visão Geral

Este projeto tem como objetivo criar um **processo completo de redundância de arquivos** utilizando recursos do **Microsoft Azure**. Através do **Azure Data Factory**, você aprenderá a configurar toda a infraestrutura necessária para mover dados entre ambientes **on-premises** e a **nuvem**, garantindo backup seguro e acessível.

## 🔄 Fluxo do Processo
1. **Conectar fontes de dados**: SQL Server local e Azure SQL Database.
2. **Criar Linked Services**: Estabelecendo conexão entre o Data Factory e os repositórios de dados.
3. **Criar Datasets**: Definição das estruturas para entrada e saída dos dados.
4. **Criar Pipelines**: Construção dos fluxos de trabalho para movimentação dos dados.
5. **Converter e armazenar**: Transformar dados em **arquivos .TXT**, organizando-os em camadas (**raw/bronze**) dentro do **Azure Data Lake**.
6. **Publicar e Executar**: Validação e execução do pipeline.
7. **Analisar performance**: Aplicando boas práticas para otimizar o processo.

---
## 🛠️ Tecnologias Utilizadas

- **Microsoft Azure** (🌍 Plataforma Cloud)
- **Azure Data Factory** (🛠 Orquestração de Dados)
- **SQL Server (On-Premises e Azure SQL Database)** (💾 Banco de Dados Relacional)
- **Azure Blob Storage** (🏢 Armazenamento de Arquivos)
- **Integration Runtime** (⚡ Conectividade Híbrida)

---
## 🗒️ Passo a Passo da Implementação

### 1. Criando o Azure Data Factory
1. Acesse o portal do **Azure**.
2. Crie um novo **Data Factory**.
3. Configure o **Integration Runtime** para conectar-se ao SQL Server local.

### 2. Configurando os Linked Services
- Adicione um **Linked Service** para o SQL Server On-Premises.
- Adicione um **Linked Service** para o Azure SQL Database.
- Adicione um **Linked Service** para o Blob Storage.

### 3. Criando os Datasets
- Crie um **Dataset** apontando para a tabela SQL de origem.
- Crie um **Dataset** para os arquivos **.TXT** de destino no Blob Storage.

### 4. Criando o Pipeline
- Adicione um **Copy Activity** para mover os dados do SQL Server para o Azure Data Lake.
- Configure a transformação dos dados em **arquivos .TXT** organizados por camadas (**raw/bronze**).
- Teste e valide as transferências.

### 5. Publicando e Executando
- Publique as alterações e execute o pipeline.
- Monitore os logs e valide a performance.

---
## 💡 Utilizando o SDK do Azure no Python
O **SDK do Azure para Python** permite interagir programaticamente com os serviços da nuvem, como o **Azure Blob Storage**. Com ele, você pode realizar operações como upload, download e gerenciamento de arquivos de forma eficiente.

Para instalar:
```bash
pip install azure-storage-blob
```

### Exemplo de código para upload de arquivo no Azure Blob Storage
```python
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
```

Confira a [documentação oficial](https://learn.microsoft.com/en-us/azure/storage/blobs/) para mais detalhes sobre suas funcionalidades.

---
## 🌟 Benefícios
- 🌐 **Alta disponibilidade**: Backup automático na nuvem.
- ⚖️ **Segurança**: Dados armazenados de forma redundante.
- ⏳ **Eficiência**: Pipelines otimizados para melhor desempenho.

---
## 💼 Contribuição
Fique à vontade para **sugerir melhorias** ou abrir um **Pull Request**! Qualquer dúvida, me chamem! 🚀

---
## 📅 Licença
Este projeto está sob a **Unlicense**, permitindo seu uso e modificação sem restrições.

---
👉 **Vamos juntos dominar o Azure!** 🌟



