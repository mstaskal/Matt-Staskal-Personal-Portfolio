--SQL statements to fill loan database tables with data--
--populate customers table--
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (122745,'Smith','John','14 Brindle St','Joliet','IL',60601);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (767905,'Johnson','Sarah','100 24th Ave','Dallas','TX',77001);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (118017,'Williams','Michael','4842 Sepulveda Blvd','Los Angeles','CA',90001);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (316181,'Brown','Jessica','12 Shool Ln','Atlanta ','GA',33101);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (631066,'Jones','Robert','202 Birch Ln','Atlanta','GA',30301);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (303049,'Garcia','Maria','303 Elm St','Phoenix','AZ',85001);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (990370,'Martinez','David','1685 A St','Long Island','NY',10001);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (852699,'Hernandez','Daniel','505 Oak Ln','Dallas','TX',75201);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (64005,'Lopez','James','606 Pine St','San Francisco','CA',94101);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (296446,'Gonzalez','Laura','707 Cedar Ave','Denver','CO',80201);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (160120,'Wilson','Anthony','808 Birch Blvd','Seattle','WA',98101);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (970599,'Anderson','Rebecca','909 Maple Dr','Portland','OR',97201);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (376934,'Thomas','Daniel','1010 Oak St','Boston','MA',2101);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (665304,'Taylor','Melissa','4547 Main St','Reno','NV',89101);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (38726,'Moore','Joshua','1212 Cedar Ln','San Diego','CA',92101);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (277217,'Jackson','Kimberly','26 Red Blvd','Denton','TX',73301);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (376641,'Martin','Kevin','1414 Maple Ave','Tampa','FL',33601);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (539547,'Lee','Amanda','23 189th St','Des Moines','IA',32801);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (635966,'Perez','Brian','1616 Pine Dr','Charlotte','NC',28201);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (928986,'White','Stephanie','1717 Cedar St','Raleigh','NC',27601);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (888129,'Harris','Patrick','1818 Birch Ave','Minneapolis','MN',55401);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (566541,'Clark','Jennifer','1919 Maple Blvd','St. Louis','MO',63101);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (328063,'Rodriguez','Adam','2020 Oak Dr','Salt Lake City','UT',84101);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (4652,'Lewis','Catherine','2121 Pine St','San Antonio','TX',78201);
INSERT INTO customers (cust_id,last,first,address,city,state,zip) VALUES (850689,'Walker','Charles','2222 Cedar Ln','Indianapolis','IN',46201);

--populate applications table--
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (396789074,250000,255102,0.98,0.42,647,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (5239875556,150000,227273,0.66,0.36,656,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (1361897393,400000,606061,0.89,0.25,695,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (6580101831,175000,265152,0.57,0.55,700,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (1966186517,300000,454545,0.95,0.37,711,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (300133868,225000,340909,0.56,0.46,717,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (7320252759,500000,757576,0.8,0.41,654,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (3156810968,350000,530303,0.98,0.4,713,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (6860888570,600000,909091,0.87,0.29,710,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (7182261084,200000,303030,0.4,0.36,714,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (9825390351,275000,416667,0.1,0.13,719,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (6496203486,320000,484848,0.9,0.18,697,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (6527894744,150000,227273,0.92,0.28,680,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (1388801426,400000,606061,0.96,0.45,703,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (2522203959,275000,416667,0.96,0.4,653,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (5369152893,180000,272727,0.97,0.3,687,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (5672818704,220000,333333,0.56,0.39,695,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (5521194712,310000,469697,0.61,0.38,698,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (9027685566,190000,287879,0.93,0.44,668,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (7266141086,250000,378788,0.89,0.22,643,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (3154528503,230000,348485,0.93,0.1,697,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (710325181,275000,416667,0.37,0.25,712,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (8353693761,320000,484848,0.7,0.46,675,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (8556835708,170000,257576,0.91,0.47,644,'Accept');
INSERT INTO applications (app_id,loan_amt,prop_value,ltv,dti,fico,decision) VALUES (1844970057,290000,439394,0.69,0.39,707,'Accept');

--populate loan_customers table--
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (364372780693,122745,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (899939719649,767905,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (390908997142,118017,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (429342979632,316181,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (667093790998,631066,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (252051542145,303049,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (571929977405,990370,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (73087652160,852699,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (830635192029,64005,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (930907433611,296446,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (315329419529,160120,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (547421347605,970599,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (456161466256,376934,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (931147722144,665304,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (839090398904,38726,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (744259034632,277217,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (624635507999,376641,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (587735254205,539547,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (75414599761,635966,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (840334895461,928986,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (225122260659,888129,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (552444655637,566541,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (211107343204,328063,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (233171384655,4652,'Primary');
INSERT INTO loan_customers (loan_num,cust_id,role) VALUES (540351658808,850689,'Primary');

--populate application_customers table--
INSERT INTO application_customers (app_id,cust_id,role) VALUES (396789074,122745,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (5239875556,767905,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (1361897393,118017,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (6580101831,316181,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (1966186517,631066,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (300133868,303049,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (7320252759,990370,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (3156810968,852699,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (6860888570,64005,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (7182261084,296446,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (9825390351,160120,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (6496203486,970599,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (6527894744,376934,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (1388801426,665304,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (2522203959,38726,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (5369152893,277217,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (5672818704,376641,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (5521194712,539547,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (9027685566,635966,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (7266141086,928986,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (3154528503,888129,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (710325181,566541,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (8353693761,328063,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (8556835708,4652,'Primary');
INSERT INTO application_customers (app_id,cust_id,role) VALUES (1844970057,850689,'Primary');

--poplate active_loans table--
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (364372780693,396789074,'123 Maple St','Chicago','IL',60601,245000,4.25,1229,300,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (899939719649,5239875556,'456 Oak Ave','Houston','TX',77001,98654,3.75,870,220,'1-Sep-23','Y');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (390908997142,1361897393,'789 Pine Blvd','Los Angeles','CA',90001,356522,5,2147,450,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (429342979632,6580101831,'101 Cedar Dr','Miami','FL',33101,100233,4.1,945,250,'1-Jun-23','Y');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (667093790998,1966186517,'202 Birch Ln','Atlanta','GA',30301,285226,4.5,1520,330,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (252051542145,300133868,'303 Elm St','Phoenix','AZ',85001,125452,3.9,1061,280,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (571929977405,7320252759,'404 Maple Rd','New York','NY',10001,400253,4.75,2608,500,'1-May-24','Y');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (73087652160,3156810968,'505 Oak Ln','Dallas','TX',75201,344652,4.2,1719,400,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (830635192029,6860888570,'606 Pine St','San Francisco','CA',94101,523214,5.1,3265,600,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (930907433611,7182261084,'707 Cedar Ave','Denver','CO',80201,80562,4,955,270,'1-Feb-22','Y');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (315329419529,9825390351,'808 Birch Blvd','Seattle','WA',98101,28256,4.65,1407,310,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (547421347605,6496203486,'909 Maple Dr','Portland','OR',97201,286774,4.35,1591,340,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (456161466256,6527894744,'1010 Oak St','Boston','MA',2101,137252,3.85,879,230,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (931147722144,1388801426,'1111 Pine Rd','Las Vegas','NV',89101,385621,5,2147,450,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (839090398904,2522203959,'1212 Cedar Ln','San Diego','CA',92101,265266,4.45,1384,300,'1-Aug-20','Y');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (744259034632,5369152893,'1313 Birch St','Austin','TX',73301,174214,3.95,852,240,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (624635507999,5672818704,'1414 Maple Ave','Tampa','FL',33601,123231,4.15,1069,260,'1-Jun-22','Y');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (587735254205,5521194712,'1515 Oak Blvd','Orlando','FL',32801,189658,4.6,1589,330,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (75414599761,9027685566,'1616 Pine Dr','Charlotte','NC',28201,177521,4.05,901,250,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (840334895461,7266141086,'1717 Cedar St','Raleigh','NC',27601,221563,4.5,1267,280,'1-Jul-22','Y');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (225122260659,3154528503,'1818 Birch Ave','Minneapolis','MN',55401,214215,4.2,1123,270,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (552444655637,710325181,'1919 Maple Blvd','St. Louis','MO',63101,102569,4.75,1434,320,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (211107343204,8353693761,'2020 Oak Dr','Salt Lake City','UT',84101,224856,4.55,1574,350,'1-Oct-24','N');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (233171384655,8556835708,'2121 Pine St','San Antonio','TX',78201,155472,3.9,800,220,'1-Jun-24','Y');
INSERT INTO active_loans (loan_num,app_id,prop_addr,prop_city,prop_state,prop_zip,upb,rate,p_i,escrow,next_due,edq) VALUES (540351658808,1844970057,'2222 Cedar Ln','Indianapolis','IN',46201,200335,4.7,1503,300,'1-Oct-24','N');

--populate rfd_codes table--
INSERT INTO rfd_codes (rfd,reason) VALUES (1,'Unemployment');
INSERT INTO rfd_codes (rfd,reason) VALUES (2,'Excessive obligations');
INSERT INTO rfd_codes (rfd,reason) VALUES (3,'Death of bwr');
INSERT INTO rfd_codes (rfd,reason) VALUES (4,'Property damage');
INSERT INTO rfd_codes (rfd,reason) VALUES (5,'Illness');
INSERT INTO rfd_codes (rfd,reason) VALUES (6,'Abandonment of property');
INSERT INTO rfd_codes (rfd,reason) VALUES (7,'Other');

--populate workout_codes table--
INSERT INTO workout_codes (workout_code,workout_type) VALUES (1,'Repayment plan');
INSERT INTO workout_codes (workout_code,workout_type) VALUES (2,'Loan modification');
INSERT INTO workout_codes (workout_code,workout_type) VALUES (3,'Forbearance');
INSERT INTO workout_codes (workout_code,workout_type) VALUES (4,'Payment deferral');
INSERT INTO workout_codes (workout_code,workout_type) VALUES (5,'Short Sale');

--populate delinquencies table--
INSERT INTO delinquencies (dq_id,loan_num,dq_amt,default_date,rfd,workout_code,cured,cure_date) VALUES (1,8.9994E+11,21015,'1-Sep-23',3,1,'N',NULL);
INSERT INTO delinquencies (dq_id,loan_num,dq_amt,default_date,rfd,workout_code,cured,cure_date) VALUES (2,4.29343E+11,4568,'1-Jun-23',4,1,'N',NULL);
INSERT INTO delinquencies (dq_id,loan_num,dq_amt,default_date,rfd,workout_code,cured,cure_date) VALUES (3,5.7193E+11,36214,'1-May-24',1,1,'N',NULL);
INSERT INTO delinquencies (dq_id,loan_num,dq_amt,default_date,rfd,workout_code,cured,cure_date) VALUES (4,9.30907E+11,16211,'1-Feb-22',6,3,'Y','1-Mar-23');
INSERT INTO delinquencies (dq_id,loan_num,dq_amt,default_date,rfd,workout_code,cured,cure_date) VALUES (5,8.3909E+11,22138,'1-Aug-20',3,4,'N',NULL);
INSERT INTO delinquencies (dq_id,loan_num,dq_amt,default_date,rfd,workout_code,cured,cure_date) VALUES (6,6.24636E+11,3622,'1-Jun-22',2,3,'Y','1-Aug-23');
INSERT INTO delinquencies (dq_id,loan_num,dq_amt,default_date,rfd,workout_code,cured,cure_date) VALUES (7,8.40335E+11,33879,'1-Jul-22',4,2,'N',NULL);
INSERT INTO delinquencies (dq_id,loan_num,dq_amt,default_date,rfd,workout_code,cured,cure_date) VALUES (8,2.33171E+11,4548,'1-Jun-24',1,2,'N',NULL);
