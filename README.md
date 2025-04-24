# Visualização de Modelos SEM com Python e Matplotlib

Este repositório contém scripts em Python para desenhar modelos de equações estruturais (SEM - *Structural Equation Modeling*) de forma programática usando `matplotlib`.

## 📌 Objetivo

Criar representações visuais claras e personalizadas de modelos SEM com variáveis latentes, relações estruturais e, opcionalmente, indicadores observados, facilitando a análise e comunicação de resultados.

## 🤖 Apoio com ChatGPT

Durante o desenvolvimento, foi necessário iterar com o ChatGPT para:

- **Corrigir a geometria das setas**, garantindo que começam e terminam nas bordas dos retângulos e não os atravessam.
- **Evitar sobreposição de elementos**, desenhando setas curvas quando necessário.
- **Reposicionar blocos** para um fluxo visual lógico e limpo.
- **Tornar o código reutilizável e parametrizável**, aplicável a diferentes modelos SEM.

Este processo iterativo permitiu alcançar um diagrama final rigoroso e visualmente claro.

---

## 🗣️ Exemplos de Prompts para ChatGPT

Aqui ficam exemplos de *prompts* genéricos que podem ser usados para obter ou melhorar este tipo de visualização:

- **Criação inicial:**
  > "Gera um diagrama SEM em matplotlib com blocos rotulados e setas entre eles, com base no seguinte modelo teórico..."

- **Ajuste visual:**
  > "As setas estão a atravessar os blocos. Por favor ajusta para que entrem e saiam das bordas dos retângulos."

- **Melhoria estética:**
  > "Algumas setas estão sobrepostas. Podes usar curvas (`arc3`) para evitar que passem por cima de blocos?"

- **Layout mais lógico:**
  > "Organiza os blocos de modo a que o fluxo do modelo vá da esquerda para a direita e de cima para baixo, evitando cruzamentos."

- **Preparação para generalização:**
  > "Transforma o código em funções reutilizáveis para que eu possa aplicar a mesma lógica a outros modelos SEM."

- **Incorporação de variáveis observadas:**
  > "Podes acrescentar os indicadores observados como caixas pequenas ligadas a cada variável latente?"

---

## 📂 Conteúdo

- `sem_diagram.py`: script principal para desenhar o modelo SEM.
- `README.md`: este ficheiro.

## 🚀 Como utilizar

1. Instalar dependências:
   ```bash
   pip install matplotlib
