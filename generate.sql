-- MySQL Script generated by MySQL Workbench
-- Fri Apr  6 15:23:09 2018
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema cruddemo
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cruddemo
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cruddemo` DEFAULT CHARACTER SET utf8 ;
USE `cruddemo` ;

-- -----------------------------------------------------
-- Table `cruddemo`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cruddemo`.`User` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NULL DEFAULT NULL,
  `email` VARCHAR(100) NOT NULL,
  `address` VARCHAR(128) NULL DEFAULT NULL,
  `gamertag` VARCHAR(100) NOT NULL,
  `profile_picture` VARCHAR(256) NULL DEFAULT 'test',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 15
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `cruddemo`.`Game`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cruddemo`.`Game` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `developer` VARCHAR(100) NOT NULL,
  `publisher` VARCHAR(100) NOT NULL,
  `price` FLOAT NOT NULL,
  `description` TEXT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cruddemo`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cruddemo`.`Order` (
  `order_number` INT NOT NULL AUTO_INCREMENT,
  `User_id` INT(11) NOT NULL,
  `Game_id` INT NOT NULL,
  PRIMARY KEY (`order_number`),
  INDEX `fk_Order_User_idx` (`User_id` ASC),
  INDEX `fk_Order_Game1_idx` (`Game_id` ASC),
  CONSTRAINT `fk_Order_User`
    FOREIGN KEY (`User_id`)
    REFERENCES `cruddemo`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Game1`
    FOREIGN KEY (`Game_id`)
    REFERENCES `cruddemo`.`Game` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
