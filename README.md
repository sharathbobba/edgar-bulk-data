# edgar-bulk-data
Programs to Transform and Structure EDGAR Bulk Datasets

The financial statement datasets are available here
https://www.sec.gov/dera/data/financial-statement-data-sets.html 
Every 3 months, a new zip file is added with the 10-Q, 10-K, 20-F and other filings.

1006 - Get the Quarterly unzipped files into files with 10K/20F/40F/10Q entries
2006 - Combine the data into Annual (10K/20F/40F) and Quarterly Files(10Q)
3006 - Annual Financial Data from the filing
4006 - Quarterly Financial Data from the filing ( to be combined into 1 program for both Annual and Quarterly. For now separate programs)
5006 - Create the financial statements for Annual and Quarterly.
6006 - (tbc) Compute Key KPIs
7006 - (tbc) Growth Rates, Analytics and Visuals

Folder Structure for Output Files

EDGAR 

EDGAR > PASS 

EDGAR > PASS > FE 

EDGAR > PASS > FE > ANN

EDGAR > PASS > FE > ANN > IS
EDGAR > PASS > FE > ANN > BS
EDGAR > PASS > FE > ANN > CF
EDGAR > PASS > FE > ANN > GEN

EDGAR > PASS > FE > QTR
EDGAR > PASS > FE > QTR > IS
EDGAR > PASS > FE > QTR > BS
EDGAR > PASS > FE > QTR > CF

