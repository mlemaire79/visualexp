# Projet ISFAC
@authors [Cédric LEVEQUE](https://github.com/CDK-Github), [Mathieu LEMAIRE](https://github.com/mlemaire79), [Gaël LEBON](https://github.com/Frenchisman)

@website www.visualexp.com

## Commandes utiles
- sudo apachectl restart
- workon visualexp
- python manage.py \<command\>
  * migrate : Actualise l’état de la base de données en accord avec l’ensemble des modèles et des migrations actuels.
  * makemigrations : Crée de nouvelles migrations sur la base des modifications détectées dans les modèles.
  * runserver : Lancer le serveur par shell sans apache (permet un débogage au besoin)

## Applications requises
- Polymorphic [Lien](http://django-polymorphic.readthedocs.io/en/latest/index.html)
