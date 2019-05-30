import random

#jugadores, equipos y acciones

alivePlayers = ['Kike','Juanma','Pavlo','Jorgito','Masterboi','Kiko','Uru','Patton','Beryan','Martinsanz','Carlos','Samu','Gon','Camer','Hugo','Xaxo']
teams = {}
actions = ['matar','alianza']

#metodos de seleccion y accion

def elegirRandom(list):
	return random.choice(list)

def pickPlayers():
	player1 = elegirRandom(alivePlayers)
	player2 = elegirRandom(alivePlayers)
	return player1,player2

def playerInTeam(player):
	for team in teams:
			if player in teams[team]:
				return team
			else:
				pass
	return False

def one2oneFight(player1,player2):
	stringAction = player1 + " mata a "+ player2+". "+player2+" queda eliminado."
	alivePlayers.remove(player2)
	return stringAction

def one2oneFightTeam(player1,player2,team2):
	stringAction = player1 + " mata a "+ player2+". "+player2+" queda eliminado."
	alivePlayers.remove(player2)
	teams[team2].remove(player2)
	return stringAction

def teamFight(team1,team2):
	tempPlayer1 = elegirRandom(teams[team1])
	tempPlayer2 = elegirRandom(teams[team2])
	stringAction = one2oneFightTeam(tempPlayer1,tempPlayer2,team2)
	if teams[team2] == []:
		stringAction = stringAction + " El equipo " + team2 + " ha sido derrotado por completo."
		teams.pop(team2,'None')
		return stringAction
	return stringAction

def formarEquipoNuevo(player1,player2):
	teamNameTemp =player1[0]+player1[1]+player1[2]+player2[0]+player2[1]+player2[2]
	teams[teamNameTemp]=[player1,player2]
	stringAction = player1+ " y "+ player2 + " se han unido en alianza formando el equipo "+ teamNameTemp
	return stringAction

def unirseaEquipo(player1,teamPlayer2):
	teams[teamPlayer2].append(player1)
	stringAction = player1 +" se ha unido al equipo "+ teamPlayer2
	return stringAction

#Accion principal
def mainAction():
	player1, player2 = pickPlayers()

	#los jugadores se vuelven a elegir si son los mismos
  while(player2 == player1):
		player2 = elegirRandom(alivePlayers)
	actionTemp = elegirRandom(actions)

  #seleccion de equipos de cada jugador
	teamPlayer1 = playerInTeam(player1)
	teamPlayer2 = playerInTeam(player2)
  
  #Si los jugadores pertenecen al mismo equipo, se acaba la accion
	if teamPlayer1 == teamPlayer2:
		if teamPlayer1 != False:
			return False
  
  #Accion de matar
	if actionTemp == 'matar':
  #si el player 1 tiene equipo
		if teamPlayer1 != False:
			if teamPlayer2 != False:
        #si ambos jugadores tienen equipo, se pelean.
				stringAction = teamFight(teamPlayer1,teamPlayer2)
				return stringAction
			#si el jugador dos NO esta en equipo, muere.
			else:
				stringAction = "El equipo compuesto por "
				for tempPlayers in teams[teamPlayer1]:
					stringAction = stringAction + " "+ tempPlayers
				stringAction = stringAction + " mata a "+player2+". "+player2+" queda eliminado."
				alivePlayers.remove(player2)
				return stringAction
        
		#si el player 1 no tiene equipo
		else:
			#si el player 2 si tiene equipo, player 1 muere.
			if teamPlayer2 != False:
				stringAction = "El equipo compuesto por "
				for tempPlayers in teams[teamPlayer2]:
					stringAction = stringAction + " "+ tempPlayers
				stringAction = stringAction + " mata a "+player1+". "+player1+" queda eliminado."
				alivePlayers.remove(player1)
				#FIN ACTION
				return stringAction
			#si el jugador dos NO esta en equipo, one to one.
			else:
				stringAction = one2oneFight(player1,player2)
				return stringAction

  #Accion de alianza
	if actionTemp == 'alianza':
  #Si ninguno tiene equipo, crean uno nuevo
		if teamPlayer1 == False:
			if teamPlayer2 == False:
				stringAction = formarEquipoNuevo(player1,player2)
				return stringAction
			else:
      #Si uno de los dos tiene equipo, se une al del otro
				stringAction = unirseaEquipo(player1,teamPlayer2)	
				return stringAction
		else:
    #Si uno de los dos tiene equipo, se une al del otro
			if teamPlayer2 == False:
				stringAction = unirseaEquipo(player2,teamPlayer1)	
				return stringAction

while alivePlayers != []:
	stringAction = mainAction()
	if stringAction == False:
		pass
	else:
		if stringAction != None:
			print(stringAction)
	if teams != {}:
		if alivePlayers == teams[list(teams.keys())[0]]:
			print("El equipo "+list(teams.keys())[0]+ "ha derrotado a todos sus rivales.")
			for team in teams:
				stringTemp = "Los jugadores "
				for player in teams[team]:
					stringTemp = stringTemp + player + ", "
				stringTemp = stringTemp + "han ganado la partida."
				print(stringTemp)
				exit()
#FIN
