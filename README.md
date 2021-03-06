# Projet ISFAC
@authors [Cédric LEVEQUE](https://github.com/CDK-Github), [Mathieu LEMAIRE](https://github.com/mlemaire79), [Gaël LEBON](https://github.com/Frenchisman)

@website www.visualexp.com

## Apres chaque pull : 
dans /var/visualexp lancer la commande 
./make.sh
(lance la mise a jour des requirements et le migrate)

## Commandes utiles
- sudo apachectl restart
- workon visualexp
- python manage.py \<command\>
  * migrate : Actualise l’état de la base de données en accord avec l’ensemble des modèles et des migrations actuels.
  * makemigrations : Crée de nouvelles migrations sur la base des modifications détectées dans les modèles.
  * runserver : Lancer le serveur par shell sans apache (permet un débogage au besoin)
  * collectstatic : récupere les fichiers se trouvant dans /static dans chaque application installée.
  * makemessages : récupere les chaines de caracteres a traduire
  * compilemassages : compile les fichiers de langue pour pouvoir les utiliser.

## Applications requises
See requirements.txt 
run with pip install -r requirements.txt

Utilisateurs de test :
admin ( super user )
Directeur ( Site Admin)
Employe (Employe)

Pass : djangodev

Pour importer les données :
python manage.py loaddata ../Data/Users.json
( python manage.py flush pour vider la base si besoin )
