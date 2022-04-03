
CREATE DATABASE IF NOT EXISTS `studentlogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `studentlogin`;

CREATE TABLE IF NOT EXISTS `studentregister` (
	`ID` int(200) NOT NULL AUTO_INCREMENT,
  	`Name` varchar(200) NOT NULL,
  	`CollegeID` varchar(200) NOT NULL,
  	`Email` varchar(200) NOT NULL,
    `MobileNumber` varchar(200) NOT NULL,
    `Password` varchar(200) NOT NULL,
    `Status` varchar(200) NOT NULL,
    PRIMARY KEY (`ID`, `CollegeID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

