create table usgsheight (
agency_cd text, 
site_no int, 
datetime text, 
tz_cd text, 
height float, 
height_accepted text
);
\copy usgsheight from 'C:\Users\Wyatt\Documents\CMU\Fall 2025\CSCI 260-001 Intro to Databases\Class\Code\usgsHeight0125-1125.txt' with delimiter E'\t';

create table usgsph (
agency_cd text,
site_no int,
datetime text,
tz_cd text,
pH float,
pH_accepted text
);
\copy usgsph from 'C:\Users\Wyatt\Documents\CMU\Fall 2025\CSCI 260-001 Intro to Databases\Class\Code\usgspH0125-1125.txt' with delimiter E'\t';

create table usgstemp (
agency_cd text,
site_no int,
datetime text,
tz_cd text,
temp float,
temp_accepted text
);
\copy usgstemp from 'C:\Users\Wyatt\Documents\CMU\Fall 2025\CSCI 260-001 Intro to Databases\Class\Code\usgsTemp0125-1125.txt' with delimiter E'\t';