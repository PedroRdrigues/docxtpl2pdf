# DOCXTPL2PDF
O objetivo do script é "rodar" em um ambiente linux com o **LibreOffice** instalado.
A distro linux utilizada foi a **Debian - Debian GNU/Linux** através do WSL.

Para realizar a instalação da distro utilizada é necessário abrir o prompt de comando e executar:
```bash
wsl --install Debian
```

Para realizar a instalação do LibreOffice no ambiente linux execute:
```bash
sudo apt update
sudo apt install libreoffice
```

Após a instalação do LibreOffice, faça um clone do repositório:
```bash
git clone https://github.com/PedroRdrigues/docxtpl2pdf.git
```

instale as bibliotecas do arquivo _requirements.txt_ (de preferencia em uma .venv):
```bash
pip install -r requirements.txt
```
Você pode realizar um teste executando o arquivo `exemple.py` dentro do diretório exemple.
