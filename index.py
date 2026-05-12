python
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the Freelancer Business Activities Dataset
dataset_url = "https://data.abudhabi/dataset/Freelancer_Business_Activities.xlsx"
data = pd.read_excel(dataset_url)
data.fillna('', inplace=True)

@app.route('/')
def home():
    categories = data['Category'].unique()
    return render_template('index.html', categories=categories)

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get("keyword")
    category = request.form.get("category")

    if category != "All":
        filtered_data = data[(data['Category'] == category) & (data['English Name'].str.contains(keyword, case=False) | data['Arabic Name'].str.contains(keyword))]
    else:
        filtered_data = data[(data['English Name'].str.contains(keyword, case=False) | data['Arabic Name'].str.contains(keyword))]

    return render_template('search_results.html', results=filtered_data.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True)
