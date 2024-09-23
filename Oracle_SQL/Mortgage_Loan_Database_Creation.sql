/*
Creation of a fictional mortgage loan database with the following tables:
All active loans
Performing loans
Delinquent loans
Properties
Borrowers
Payment history
Delinquency codes

Tables created using MS Excel, Python, and Oracle SQL*/

/*Python code for creating the SQL INSERT INTO statements:

1) LoanInfo class definition:

class LoanInfo:
    def __init__(self,loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd):
        self.loan_num = loan_num
        self.bwr_last = bwr_last
        self.bwr_first = bwr_first
        self.address = address
        self.city = city
        self.st = st
        self.zip = zip
        self.loan_amt = loan_amt
        self.rate = rate
        self.upb = upb
        self.ltv = ltv
        self.monthlyPI = monthlyPI
        self.monthlyEscrow = monthlyEscrow
        self.next_payment_due = next_payment_due
        self.delinquent = delinquent
        self.rfd = rfd

2) Generate list of random loan numbers:

import random
loan_list = []
for i in range(1,26):
    loan_number = random.randint(1,999999999)
    loan_list.append(loan_number)
for i in loan_list:
    print(i)

3) Python script to create SQL statement

with open(
        'C:/Users/13199/Desktop/Matts/Data_Portfolio/Loan_list.csv') as loan_csv:
    csv_reader = csv.reader(loan_csv, delimiter=',')
    line_count = 0
    loan_group = {}
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        loan_group[str(row[0])] = LoanInfo(str(row[0]), row[1], row[2], str(row[3]), str(row[4]), str(row[5]), str(row[6]), row[7],row[8],row[9],row[10],row[11],row[12],str(row[13]),str(row[14]),str(row[15]))


    for key, value in loan_group.items():
        print(f'INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) '
              f'VALUES ({loan_group[key].loan_num},\'{loan_group[key].bwr_last}\',\'{loan_group[key].bwr_first}\',\'{loan_group[key].address}\',\'{loan_group[key].city}\',\'{loan_group[key].st}\',{loan_group[key].zip},'
              f'{loan_group[key].loan_amt},{loan_group[key].rate},{loan_group[key].upb},{loan_group[key].ltv},{loan_group[key].monthlyPI},{loan_group[key].monthlyEscrow},\'{loan_group[key].next_payment_due}\',\'{loan_group[key].delinquent}\',\'{loan_group[key].rfd}\');')
*/

DROP TABLE active_loans PURGE;

CREATE TABLE active_loans 
	(loan_num VARCHAR2(12),
	bwr_last VARCHAR2(25),
	bwr_first VARCHAR2(25),
	address VARCHAR2(25),
	city VARCHAR2(25),
	st CHAR(2),
	zip CHAR(5),
	loan_amt NUMBER(11,2),
	rate NUMBER (6,3),
	upb NUMBER(11,2),
	ltv NUMBER(6,3),
	monthlyPI NUMBER(11,2),
	monthlyEscrow NUMBER(11,2),
	next_payment_due DATE,
	delinquent CHAR(1),
	rfd VARCHAR2(100),
		CONSTRAINT active_loans_loan_num_pk PRIMARY KEY (loan_num));

INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (314174313,'Smith','John','123 Maple St','Chicago','IL',60601,250000.00,4.25,245000,0.98,1229,300,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (588128788,'Johnson','Sarah','456 Oak Ave','Houston','TX',77001,150000.00,3.75,98654,0.657693333,870,220,'1-Sep-23','Y','Medical expenses');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (268367496,'Williams','Michael','789 Pine Blvd','Los Angeles','CA',90001,400000.00,5,356522,0.891305,2147,450,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (45184254,'Brown','Jessica','101 Cedar Dr','Miami','FL',33101,175000.00,4.1,100233,0.57276,945,250,'1-Jun-23','Y','Unemployment');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (457059756,'Jones','Robert','202 Birch Ln','Atlanta','GA',30301,300000.00,4.5,285226,0.950753333,1520,330,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (302719164,'Garcia','Maria','303 Elm St','Phoenix','AZ',85001,225000.00,3.9,125452,0.557564444,1061,280,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (401579210,'Martinez','David','404 Maple Rd','New York','NY',10001,500000.00,4.75,400253,0.800506,2608,500,'1-May-24','Y','Business failure');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (958027632,'Hernandez','Da','505 Oak Ln','Dallas','TX',75201,350000.00,4.2,344652,0.98472,1719,400,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (949046800,'Lopez','James','606 Pine St','San Francisco','CA',94101,600000.00,5.1,523214,0.872023333,3265,600,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (997953032,'Gonzalez','Laura','707 Cedar Ave','Denver','CO',80201,200000.00,4,80562,0.40281,955,270,'1-Feb-22','Y','Marital');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (424113125,'Wilson','Anthony','808 Birch Blvd','Seattle','WA',98101,275000.00,4.65,28256,0.102749091,1407,310,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (632403590,'Anderson','Rebecca','909 Maple Dr','Portland','OR',97201,320000.00,4.35,286774,0.89616875,1591,340,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (157758446,'Thomas','Daniel','1010 Oak St','Boston','MA',2101,150000.00,3.85,137252,0.915013333,879,230,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (432008011,'Taylor','Melissa','1111 Pine Rd','Las Vegas','NV',89101,400000.00,5,385621,0.9640525,2147,450,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (723136345,'Moore','Joshua','1212 Cedar Ln','San Diego','CA',92101,275000.00,4.45,265266,0.964603636,1384,300,'1-Aug-20','Y','Unemployment');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (353555123,'Jackson','Kimberly','1313 Birch St','Austin','TX',73301,180000.00,3.95,174214,0.967855556,852,240,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (610336202,'Martin','Kevin','1414 Maple Ave','Tampa','FL',33601,220000.00,4.15,123231,0.560140909,1069,260,'1-Jun-22','Y','Medical expenses');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (817254072,'Lee','Amanda','1515 Oak Blvd','Orlando','FL',32801,310000.00,4.6,189658,0.6118,1589,330,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (915813726,'Perez','Brian','1616 Pine Dr','Charlotte','NC',28201,190000.00,4.05,177521,0.934321053,901,250,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (853060616,'White','Stephanie','1717 Cedar St','Raleigh','NC',27601,250000.00,4.5,221563,0.886252,1267,280,'1-Jul-22','Y','Unemployment');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (606911942,'Harris','Patrick','1818 Birch Ave','Minneapolis','MN',55401,230000.00,4.2,214215,0.931369565,1123,270,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (489737273,'Clark','Jennifer','1919 Maple Blvd','St. Louis','MO',63101,275000.00,4.75,102569,0.372978182,1434,320,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (508454862,'Rodriguez','Adam','2020 Oak Dr','Salt Lake City','UT',84101,320000.00,4.55,224856,0.702675,1574,350,'1-Oct-24','N','');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (218395081,'Lewis','Catherine','2121 Pine St','San Antonio','TX',78201,170000.00,3.9,155472,0.914541176,800,220,'1-Jun-24','Y','Medical expenses');
INSERT INTO active_loans (loan_num,bwr_last,bwr_first,address,city,st,zip,loan_amt,rate,upb,ltv,monthlyPI,monthlyEscrow,next_payment_due,delinquent,rfd) VALUES (303689231,'Walker','Charles','2222 Cedar Ln','Indianapolis','IN',46201,290000.00,4.7,200335,0.690810345,1503,300,'1-Oct-24','N','');
