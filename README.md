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

