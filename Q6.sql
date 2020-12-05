DROP PROCEDURE IF EXISTS playerSchedule;

DELIMITER //

CREATE PROCEDURE playerSchedule(IN name VARCHAR(20))
BEGIN
  SELECT playerName, against, gameTime, snack, coachName
  FROM (SELECT Players.playerName, against, gameTime, snack, 
  teamName 
  FROM (SELECT * FROM (SELECT playerName, awayTeam AS 
  against, gameTime, 1 AS snack 
  FROM (Games INNER JOIN Players ON Games.homeTeam = Players.teamName) 
  WHERE homeTeam IN (SELECT teamName FROM Players) 
  UNION SELECT playerName, homeTeam AS against, gameTime, 0 AS snack 
  FROM (Games INNER JOIN Players ON Games.awayTeam = Players.teamName) 
  WHERE awayTeam IN (SELECT teamName FROM Players)) AS table1 
  WHERE name = playerName ORDER BY gameTime) AS table2 
  INNER JOIN Players ON table2.playerName = Players.playerName) AS 
  table3 INNER JOIN Teams ON table3.teamName = Teams.teamName;
END //

DELIMITER ;