 # ATP_self_filling_kettle

ATP eindopdracht gemaakt door Dylan Griffioen

Dit project heeft drie uitvoerbare python files.

main.py:
- Dit vraagt de temperatuur en het waterniveau op en voert daarmee de controle functies eenmalig uit
- Dit heeft de python c++ binding
- Deze file is uitgevoerd en getest doormiddel van invoke via msys2 specefiek msys2 mingww64 (kan niet garanderen dat dit werkt via powershell of cmd)

test.py
- Dit heeft alle testen die uitgevoerd moesten worden om te bevestigen dat het systeem werkt naar behoren
- Kan gerund worden via powershell of cmd

simulator.py
- Dit heeft de simulatie van het systeem
- Standaard staat in deze file de simulatie op user input mode, dit betekend dat de user gevraagd word om y in te voeren om de waterkoker van de load cell af te halen en om y in te drukken om de waterkoker weer op de load cell te zetten
- Dit simuleert de user input die later ook nodig is voor het systeem
- De simulatie kan ook op auto mode gezet waarmee het systeem dit zelfstandig doet
- De simulatie heeft een sleep functie om het leesbaar te houden in de cli die standaard op 1 seconde staat (in auto mode is het aan te raden om dit te verhogen)