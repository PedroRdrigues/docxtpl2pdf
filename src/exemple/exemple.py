from docxtpl2pdf import convert_template_to_pdf

# Informações que vem com a requisição
context = {
    "title": "teste",
    "author": "Athor",
    "nome": "Seu nome",
    "email": "email@exmplo.com",
    "caixaTxt": "Texto na caixa de texto"
}

# Preenchimento dos valores e conversão para .pdf
template_docx = convert_template_to_pdf(
    "./templates/teste.docx",
    context
)

# Lê os bytes e salva em um arquivo.
nome_arquivo_saida = "./saves/resultado_final.pdf"
with open(nome_arquivo_saida, "wb") as f_out:
    f_out.write(template_docx)
print(f"Arquivo salvo com sucesso: {nome_arquivo_saida}")
