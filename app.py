from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def dashboard():
    anos = np.array([2020, 2021, 2022, 2023])
    vendas = np.array([454932, 906032, 1298434, 1775159])

    coef = np.polyfit(anos, vendas, 1)
    poly1d_fn = np.poly1d(coef)

    ano_2024 = 2024
    vendas_2024 = poly1d_fn(ano_2024)

    db = {
        '2020': {
            'modelo': "Model Y",
            'vendas': 454932,
            'vendas_futuras': 480000
        },
        '2021': {
            'modelo': "Model Y",
            'vendas': 906032,
            'vendas_futuras': 520000
        },
        '2022': {
            'modelo': "Model Y",
            'vendas': 1298434,
            'vendas_futuras': 580000
        },
        '2023': {
            'modelo': "Model Y",
            'vendas': 1775159,
            'vendas_futuras': 620000
        },
        '2024': {
            'modelo': "Model Y",
            'vendas': vendas_2024,
            'vendas_futuras': None 
        },
        '2025': {
            'modelo': "Model Y",
            'vendas': "em construção",
            'vendas_futuras': None
        }
    }
    return render_template('dashboard.html', sales_data=db)

if __name__ == '__main__':
    app.run(debug=True)
