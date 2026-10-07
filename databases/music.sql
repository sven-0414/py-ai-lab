CREATE TABLE students (
	student_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE teachers (
	teacher_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE instruments (
	instrument_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE lessons (
	lesson_id INTEGER PRIMARY KEY,
	teacher_id INTEGER,
	instrument_id INTEGER,
	date TEXT,
	time TEXT,
	room TEXT,
	FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
	FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);

CREATE TABLE lesson_students (
	lesson_id INTEGER,
	student_id INTEGER,
	PRIMARY KEY (lesson_id, student_id),
	FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id),
	FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE teacher_instruments (
	teacher_id INTEGER,
	instrument_id INTEGER,
	PRIMARY KEY (teacher_id, instrument_id),
	FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
	FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);