import streamlit as st
import pandas as pd

def main():
    st.title("Primeira Versão")
    df = carregarDados()  # Carrega os dados e exibe a tabela
    st.subheader('Tabela de Dados')
    st.write(df)  # Exibe a tabela
    st.subheader('Gráfico de Salário por Funcionários')
    st.bar_chart(df.set_index('Nome')['Salário'])  # Exibe o gráfico

def carregarDados():
    # Simulador de um carregamento de dados
    data = {
        'Nome': ['Maria', 'José', 'Rafael', 'Raimunda'],
        'Idade': [24, 56, 34, 44],
        'Salário': [3000, 4000, 6000, 7000]
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    main()