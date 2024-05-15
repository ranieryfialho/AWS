import streamlit as st
import pandas as pd

def main():
    st.title("Primeira Versão")
    st.write(carregarDados())  

def carregarDados():
    # simulador de um carregamento de dados
    data = {
        'Nome': ['Maria', 'José', 'Rafael', 'Raimunda'],
        'Idade': [24, 56, 34, 44],
        'Salário': [3000, 4000, 6000, 7000]
    }
    df = pd.DataFrame(data)
    st.subheader('Gráfico de Salário por funcionários')
    st.bar_chart(data, x='Nome', y='Salário') 
    return df


if __name__ == "__main__":
    main()