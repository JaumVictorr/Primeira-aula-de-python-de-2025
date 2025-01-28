from flask import Flask,jsonify
from main import app, con

@app.route('/Livro', methods=['GET'])
def livro():
    cur = con.cursor()
    cur.execute('SELECT ID_Livro, titulo, autor, ano_publicacao')
    livros = cur.fetchall()
    livros.dic = []
    for livro in livros:
        livro.dic.append({
            'id': livro[0],
            'titulo': livro[1],
            'autor': livro[2],
            'ano_publicacao': livro[3]
        })
        return jsonify(mensagem='Lista de Livros', livros=livros_dic)
