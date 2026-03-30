from docxtpl import DocxTemplate
import subprocess
import tempfile
import os
from typing import Any

def convert_template_to_pdf(template: str, context: dict[str,Any] | None = None) -> Any:
    # 1. Cria o diretório temporário
    with tempfile.TemporaryDirectory() as tmp_dir:
        print(f"Pasta temporária criada em: {tmp_dir}")

        docx = os.path.join(tmp_dir, "documento.docx")

        # Faz a troca dos Placesholders no template pelos valores informados no context
        doc = DocxTemplate(template)
        doc.render(context)
        doc.save(docx)

        # Configura o comando para conversão
        command = [
            'libreoffice',
            '--headless',
            '--convert-to', 'pdf',
            '--outdir', tmp_dir,
            docx
        ]

        try:
            # Executa o comando de conversão, o arquivo .docx é convertido para um .pdf com o mesmo nome
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            pdf = os.path.join(tmp_dir, "documento.pdf")

            # Verifica se o arquivo existe e, caso sim, retorna os bytes
            if os.path.exists(pdf):
                with open(pdf, "rb") as f:
                    return f.read()
        except Exception as e:
            raise Exception("Erro ao converter o arquivo .docx para .pdf:\n", e)
