create database dbms_medicine;
CREATE TABLE `dbms_medicine`.`medicine` (
  `medicine_id` VARCHAR(4) NOT NULL,
  `medicine_name` VARCHAR(10) NULL,
  `medicine_cost` INT NULL,
  `medicine_brand` VARCHAR(10) NULL,
  PRIMARY KEY (`medicine_id`));

INSERT INTO `dbms_medicine`.`medicine` (`medicine_id`, `medicine_name`, `medicine_cost`, `medicine_brand`) VALUES ('1001', 'Ranbaxy', '50', 'Aimway');
INSERT INTO `dbms_medicine`.`medicine` (`medicine_id`, `medicine_name`, `medicine_cost`, `medicine_brand`) VALUES ('1002', 'Mifoxine', '40', 'Pargua');

CREATE TABLE `dbms_medicine`.`batch` (
  `batch_no` VARCHAR(4) NOT NULL,
  `medicine_stock` INT NULL,
  `manufacture_date` DATETIME NULL,
  `expiry_date` DATETIME NULL,
  `med_id` varchar(4) NOT NULL,
  PRIMARY KEY (`batch_no`));

INSERT INTO `dbms_medicine`.`batch` (`batch_no`, `medicine_stock`, `manufacture_date`, `expiry_date`,`med_id`) VALUES ('B101', '20', '2020-09-16', '2021-03-16','1001');
INSERT INTO `dbms_medicine`.`batch` (`batch_no`, `medicine_stock`, `manufacture_date`, `expiry_date`,`med_id`) VALUES ('B201', '30', '2020-09-24', '2021-03-24','1002');

CREATE TABLE `dbms_medicine`.`sales` (
  `sale_id` VARCHAR(4) NOT NULL,
  `medicine_id` VARCHAR(4) NULL,
  `medicine_cost` INT NULL,
  `batch_id` VARCHAR(4) NULL,
  `quantity` INT NULL,
  `amount` INT NULL,
  PRIMARY KEY (`sale_id`));

INSERT INTO `dbms_medicine`.`sales` (`sale_id`, `medicine_id`, `medicine_cost`, `batch_id`, `quantity`) VALUES ('S101', '1001', '50', 'B101', '20');

CREATE TABLE `dbms_medicine`.`sale_details` (
  `sale_date` DATE NOT NULL,
  `sale_id` VARCHAR(4) NOT NULL,
  `user_id` VARCHAR(8) NOT NULL,
  `org_id` VARCHAR(4) NOT NULL,
  PRIMARY KEY (`sale_id`, `user_id`, `org_id`));

INSERT INTO `dbms_medicine`.`sale_details` (`sale_date`, `sale_id`, `user_id`, `org_id`) VALUES (curdate(), 'S101', 'Adi', 'O101');

CREATE TABLE `dbms_medicine`.`organisation` (
  `org_id` VARCHAR(4) NOT NULL,
  `org_name` VARCHAR(10) NULL,
  `org_type` VARCHAR(10) NULL,
  `contact_no` INT NULL,
  PRIMARY KEY (`org_id`));

INSERT INTO `dbms_medicine`.`organisation` (`org_id`, `org_name`, `org_type`, `contact_no`) VALUES ('O101', 'Texas med', 'purchase', '990293928');
INSERT INTO `dbms_medicine`.`organisation` (`org_id`, `org_name`, `org_type`, `contact_no`) VALUES ('O102', 'Filla Co', 'purchase', '622114488');

CREATE TABLE `dbms_medicine`.`user_info` (
  `username` VARCHAR(20) NOT NULL,
  `phone_number` VARCHAR(10) NULL,
  `email` VARCHAR(20) NULL,
  `street_user` VARCHAR(15) NULL,
  `user_city` VARCHAR(10) NULL,
  `user_state` VARCHAR(10) NULL,
  `pincode` VARCHAR(6) NULL,
  PRIMARY KEY (`username`));

INSERT INTO `dbms_medicine`.`user_info` (`username`, `phone_number`, `email`, `street_user`, `user_city`, `user_state`, `pincode`) VALUES ('Adi', '9123876321', 'adi@gmail.com', 'Hazira road', 'Surat', 'Gujarat', '394270');
INSERT INTO `dbms_medicine`.`user_info` (`username`, `phone_number`, `email`, `street_user`, `user_city`, `user_state`, `pincode`) VALUES ('Devesh', '7786923413', 'devesh@gmail.com', 'VIT university', 'Vellore', 'Tamil Nadu', '632014');

CREATE TABLE `dbms_medicine`.`login` (
  `Login_id` VARCHAR(4) NOT NULL,
  `Login_username` VARCHAR(20) NULL,
  `Login_password` VARCHAR(20) NULL,
  PRIMARY KEY (`Login_id`));

INSERT INTO `dbms_medicine`.`login` (`Login_id`, `Login_username`, `Login_password`) VALUES ('L101', 'Adi', 'adi.thakkar');
INSERT INTO `dbms_medicine`.`login` (`Login_id`, `Login_username`, `Login_password`) VALUES ('L102', 'Devesh', 'devesh.dr');

CREATE TABLE `dbms_medicine`.`role` (
  `Role_id` VARCHAR(20) NOT NULL,
  `role_type` VARCHAR(10) NULL,
  `role_user_id` VARCHAR(20) NULL,
  PRIMARY KEY (`Role_id`));

INSERT INTO `dbms_medicine`.`role` (`Role_id`, `role_type`, `role_user_id`) VALUES ('R101', 'Manager', 'L101');
INSERT INTO `dbms_medicine`.`role` (`Role_id`, `role_type`, `role_user_id`) VALUES ('R102', 'Employee', 'L102');
