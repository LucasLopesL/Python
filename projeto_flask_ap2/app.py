from flask import Flask, render_template

app = Flask(__name__)

# Criação da primeira página
# Route
@app.route("/")
# Função
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contato():
    return render_template("contatos.html")

# Colocar o site no ar
if __name__ == "__main__":
   app.run(debug=True)
