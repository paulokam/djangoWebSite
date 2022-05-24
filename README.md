# My First Django WebPage


# Pre-Requisitos

- Você pode encontrar as bibliotecas pré-requisitadas no arquivo requirements.txt
- Não esqueceça de baixar o [Docker](https://docs.docker.com/get-docker/) para uma melhor utilização do programa.
- As bibliotecas são automaticamente instaladas com os comandos abaixo, caso o Docker seja utilizado.

# Como rodar o projeto

- Para executar o servidor local, execute o comando no terminal dentro do diretório django-websites:
```
docker-compose up --build
```
- Alternativamente, você pode executar ele em segundo plano utilizando dos seguintes comandos:
```
docker-compose up -d   // Para iniciar
docker-compose down    // Para parar
```

- Não esqueça de rodar as migrations caso faça alguma alteração nos arquivos:
```
docker-compose exec web python manage.py migrate
```

- Caso achar necessário criar um superuser para acessar a interface de admin:
```
docker-compose exec web python manage.py createsuperuser
```

- Por comodidade, um admin base já foi criado:
```
username: admin
password: admin
```

# Como acessar o servidor
Por fim, acesse o site neste link: [http://localhost:8000/](http://localhost:8000/)

Para acessar o diretório de admin: [http://localhost:8000/admin](http://localhost:8000/admin)


Permaneço à disposição.

# Referências
- [Repostitório tutorial-e-commerce-django](https://github.com/fabioruicci/tutorial-e-commerce-django)