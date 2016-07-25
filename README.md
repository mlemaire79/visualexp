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

## Variables de couleurs LESS
/* 
Entity : Elements qui doivent ressortir du plan, tels que les boutons,
autre éléments qui possèderont une propriété :hover etc
*/

/*****************************************/
/************* TEINTES BLEU **************/
/*****************************************/

@bColor-bg:                  rgba(0, 105, 135, 1);
@bColor-entity:              rgba(167, 236, 255, 1);
@bColor-hover-entity:        rgba(0, 81, 104, 1);
@bColor-font:                rgba(117, 225, 255, 1);
@bColor-font-entity:         rgba(0, 81, 104, 1);
@bColor-font-hover-entity:   rgba(167, 236, 255, 1);
@bColor-link:                rgba(167, 236, 255, 1);

/*****************************************/
/************* TEINTES ROUGE *************/
/*****************************************/

@rColor-entity:              rgba(165, 0, 4, 1);
@rColor-hover-entity:        rgba(255, 164, 166, 1);
@rColor-active-entity:       rgba(255, 112, 116, 1);
@rColor-font-entity:         rgba(255, 112, 116, 1);
@rColor-font-hover-entity:   rgba(165, 0, 4, 1);
@rColor-font-active-entity:  rgba(165, 0, 4, 1);
@rColor-icon-entity:         rgba(255, 0, 7, 1);

/*****************************************/
/************* TEINTES JAUNE *************/
/*****************************************/

@yColor-entity:              rgba(255, 188, 0, 1);
@yColor-font:                rgba(255, 218, 112, 1);
@yColor-font-container:      rgba(167, 123, 0, 1);
@yColor-container:           rgba(255, 218, 112, 1);
