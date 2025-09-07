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
| Breast Cancer (MSK, Cancer Cell 2018) | cBioPortal | ODbL |
| Metastatic Breast Cancer (MSK, Cancer Discovery 2022) | cBioPortal | ODbL |
| Breast Invasive Carcinoma (TCGA, Firehose Legacy) | cBioPortal | TCGA Data Usage Policy |
| Breast Cancer (METABRIC, Nature 2012 & Nat Commun 2016) | cBioPortal | ODbL |
| MSK-CHORD (MSK, Nature 2024) | cBioPortal | Creative Commons |

> **Nota:** Todos os datasets são usados em conformidade com suas licenças. Mais detalhes em DATA_LICENSES.

---

## Instalação

#### Windows

   - python -m venv venv
   - venv\Scripts\activate
   - pip install -r requirements.txt
   - pip install -e .

#### MacOs/Linux

   - python -m venv venv
   - source venv/bin/activate
   - pip install -r requirements.txt
   - pip install -e .
   

 **Observação:** Execute o codigo **a partir da raiz do projeto**, onde está localizado o arquivo `requirements.txt`