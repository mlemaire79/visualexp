#!/bin/bash
#MAJ du fichier de traduction
#workon visualexp
cd /var/visualexp/visualexpcode/visualexpcode

langues=( "en" "de" "ru" "zh")

for element in "${langues[@]}"    
do   
       django-admin makemessages -l $element -e py,html
done