
## Project Structure

```
├── first_proj # Pasta do projeto de Django
│ ├── asgi.py # Modulo que executa o ASGI (Async Server Gateway Interfaz)do projeto 
│ ├── __init__.py # modulo que indica que as pasta é um pacote.
│ ├── settings.py # Modulo onde se espeficia as configurações do django.
│ ├── urls.py #  # modulo onde se configurão as URL do Django
│ └── wsgi.py # Modulo que executa o WSGI (Web Server Gateway Interface) do projeto.
├── manage.py # Arquivo cental de Django para interagir com o projeto.
├── Procfile # Arquivo de configuração do HEROKU para definir os processos a executar.
├── README.md # documentação escrita em markdown do projeto.
├── requirements.txt  # o arquivo que esta listando as librerias que o projeto precisa para funcionar.
```