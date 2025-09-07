# Previsão de Recorrência de Câncer de Mama

## Descrição
Este projeto utiliza dados genômicos e clínicos de câncer de mama para **desenvolver modelos de machine learning que preveem a recorrência do tumor**. Inclui análise exploratória, pré-processamento de dados e avaliação de modelos preditivos.

---

## Objetivo
- Construir um **modelo de ML para prever recorrência de câncer de mama**.  
- Identificar **genes e características clínicas** que influenciam a recorrência.  
- Avaliar modelos com métricas como **acurácia, AUC, precisão e recall**.

---

## Datasets
| Nome | Fonte | Licença |
|---------|-------|---------|
| Breast Cancer (MSK, Cancer Cell 2018) | cBioPortal | Custom / sob registro |
| Metastatic Breast Cancer (MSK, Cancer Discovery 2022) | cBioPortal | CC BY-NC-ND 4.0 |
| Breast Invasive Carcinoma (TCGA, Firehose Legacy) | cBioPortal | CC BY-NC-ND 4.0 |
| Breast Cancer (METABRIC, Nature 2012 & Nat Commun 2016) | cBioPortal | TCGA Data Use Policy |
| MSK-CHORD (MSK, Nature 2024) | cBioPortal | Creative Commons |

> **Nota:** Todos os datasets são usados em conformidade com suas licenças. Mais detalhes em DATA_LICENSES.

---

## Instalação

#### Windows

   >> python -m venv venv
   >> venv\Scripts\Activate
   >> pip install -r requirements.txt


#### MacOs/Linux

   >> python -m venv venv
   >> source venv/Scripts/Activate
   >> pip install -r requirements.txt
   

 **Observação:** Execute o codigo **a partir da raiz do projeto**, onde está localizado o arquivo `requirements.txt`