UPDATE Games SET homeWin = CASE 
	WHEN gameID = 0 THEN 0
	WHEN gameID = 1 THEN 0
	WHEN gameID = 2 THEN 1
	WHEN gameID = 3 THEN 0
	WHEN gameID = 4 THEN 1
	WHEN gameID = 5 THEN 0
	WHEN gameID = 6 THEN 0
	WHEN gameID = 7 THEN 1
	WHEN gameID = 8 THEN -1
	WHEN gameID = 9 THEN 0
	WHEN gameID = 10 THEN 0
	WHEN gameID = 11 THEN 1
	WHEN gameID = 12 THEN 0
	WHEN gameID = 13 THEN 1
	WHEN gameID = 14 THEN 0
END;

UPDATE Games SET awayWin = CASE 
	WHEN gameID = 0 THEN 1
	WHEN gameID = 1 THEN 1
	WHEN gameID = 2 THEN 0
	WHEN gameID = 3 THEN 1
	WHEN gameID = 4 THEN 0
	WHEN gameID = 5 THEN 1
	WHEN gameID = 6 THEN 1
	WHEN gameID = 7 THEN 0
	WHEN gameID = 8 THEN -1
	WHEN gameID = 9 THEN 1
	WHEN gameID = 10 THEN 1
	WHEN gameID = 11 THEN 0
	WHEN gameID = 12 THEN 1
	WHEN gameID = 13 THEN 0
	WHEN gameID = 14 THEN 1
END;

SELECT Team, SUM(W) AS W, SUM(T) AS T ,SUM(L) AS L FROM 
(SELECT * FROM 
(SELECT * FROM 
(SELECT Team, SUM(Win) AS W , 0 AS T, 0 AS L FROM 
(SELECT * FROM 
(SELECT awayTeam AS Team, COUNT(*) AS Win FROM Games WHERE 
awayWin = 1 GROUP BY awayTeam) AS awayWins UNION 
(SELECT homeTeam AS Team, COUNT(*) AS Win FROM Games WHERE 
homeWin = 1 GROUP BY homeTeam)) AS Wins GROUP BY Team) AS Wins UNION 
(SELECT Team, 0 AS W, 0 AS T, SUM(Win) AS L FROM 
(SELECT * FROM 
(SELECT awayTeam AS Team, COUNT(*) AS Win FROM Games WHERE 
awayWin = 0 GROUP BY awayTeam) AS awayWins UNION 
(SELECT homeTeam AS Team, COUNT(*) AS Win FROM Games WHERE 
homeWin = 0 GROUP BY homeTeam)) AS Wins GROUP BY Team)) AS winLoss UNION 
(SELECT Team, 0 AS W, SUM(Win) AS T, 0 AS L FROM 
(SELECT * FROM 
(SELECT awayTeam AS Team, COUNT(*) AS Win FROM Games WHERE 
awayWin = -1 GROUP BY awayTeam) AS awayWins UNION 
(SELECT homeTeam AS Team, COUNT(*) AS Win FROM Games WHERE 
homeWin = -1 GROUP BY homeTeam)) AS Wins GROUP BY Team)) AS WTL GROUP BY Team;