CREATE TABLE Student
(
  Gender VARCHAR(20) NOT NULL,
  Ethnicity VARCHAR(20) NOT NULL,
  Student_ID INT NOT NULL,
  PRIMARY KEY (Student_ID)
);

CREATE TABLE TestID_TestName
(
  Test_ID INT NOT NULL,
  Test_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (Test_ID)
);

CREATE TABLE LevelID_LevelName
(
  Level_ID INT NOT NULL,
  Level_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (Level_ID)
);

CREATE TABLE Results
(
  Score INT NOT NULL,
  Student_ID INT NOT NULL,
  Test_ID INT NOT NULL,
  Level_ID INT NOT NULL,
  PRIMARY KEY (Student_ID, Test_ID, Level_ID),
  FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
  FOREIGN KEY (Test_ID) REFERENCES TestID_TestName(Test_ID),
  FOREIGN KEY (Level_ID) REFERENCES LevelID_LevelName(Level_ID)
);