# My First Django WebPage


# Como rodar o projeto

- No terminal, execute o comando
```
docker-compose up --build
```

- Não esqueça de rodar as migrations:
```
docker-compose exec web python manage.py migrate
```

- Não esqueça de criar um superuser para acessar a interface de admin (caso achar necessário):
```
docker-compose exec web python manage.py createsuperuser
```

Por fim, acesse o site neste link: [http://localhost:8000/](http://localhost:8000/)

Permaneço à disposição.

# Referências
- [Repostitório tutorial-e-commerce-django](https://github.com/fabioruicci/tutorial-e-commerce-django)