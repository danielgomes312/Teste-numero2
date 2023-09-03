# # o

# import random

# HOME_TEAM_WON = 1

# def tournamentWinner(competitions, results):
#     currentBestTeam = ""
#     scores = {currentBestTeam: 0}
#     HOME_TEAM_WON = 1
    
#     for idx, competition in enumerate(competitions):
#         result = results[idx]
#         homeTeam, awayTeam = competition

#         winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

#         updateScores(winningTeam, 3, scores)

#         if scores[winningTeam] > scores[currentBestTeam]:
#             currentBestTeam = winningTeam

#     return currentBestTeam

# def updateScores(team, points, scores):
#     if team not in scores:
#         scores[team] = 0

#     scores[team] += points


# competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
# results = random.randint(-1,2)

# resultado = tournamentWinner(competitions, results)
# print(results)



# MAKING A RANDOM NUMBER

import random

def criar_array_numeros_aleatorios(n, min_valor, max_valor):
    # Gera uma lista de n números aleatórios no intervalo [min_valor, max_valor]
    numeros_aleatorios = [random.randint(min_valor, max_valor) for _ in range(n)]
    
    # Converte a lista de números em uma string com números separados por vírgulas
    numeros_separados_por_virgula = ','.join(map(str, numeros_aleatorios))
    
    return numeros_separados_por_virgula

# Exemplo de uso da função para criar uma string com 10 números aleatórios entre 1 e 100
string_numeros_aleatorios = criar_array_numeros_aleatorios(10, 1, 100)
print(string_numeros_aleatorios)



def tournamentWinner(competitions, results):
    # Initialize a variable to keep track of the current best team
    currentBestTeam = ""
    
    # Create a dictionary to store the scores, starting with an empty team and 0 points
    scores = {currentBestTeam: 0}
    
    # Iterate through the competitions and results using an index
    for idx, competition in enumerate(competitions):
        # Get the result (whether the home team or away team won) for the current competition
        result = results[idx]
        
        # Extract the home team and away team from the current competition
        homeTeam, awayTeam = competition

        # Determine the winning team based on the result
        # If the home team won, set winningTeam to homeTeam; otherwise, set it to awayTeam
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        # Call the updateScores function to add 3 points to the winning team's score
        updateScores(winningTeam, 3, scores)

        # Check if the winning team has a higher score than the current best team
        if scores[winningTeam] > scores[currentBestTeam]:
            # If yes, update the current best team to be the winning team
            currentBestTeam = winningTeam

    # After iterating through all competitions, return the current best team, which is the winner
    return currentBestTeam

# Function to update the scores for a team in the scores dictionary
def updateScores(team, points, scores):
    # If the team is not in the scores dictionary, add it with an initial score of 0
    if team not in scores:
        scores[team] = 0

    # Increment the team's score by the specified number of points
    scores[team] += points

