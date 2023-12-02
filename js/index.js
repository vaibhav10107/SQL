const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('mydatabase.db');

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter the Name: \n', (name) => {
    rl.question('Enter the Age: \n', (age) => {
        rl.question('Enter the Department: \n', (department) => {
            rl.question('Enter the Place: \n', (place) => {
                db.serialize(() => {
                    db.run("CREATE TABLE IF NOT EXISTS Employees (ID INTEGER PRIMARY KEY, Name TEXT, Age INTEGER, Department TEXT, Place TEXT)");

                    const stmt = db.prepare("INSERT INTO Employees (Name, Age, Department, Place) VALUES (?, ?, ?, ?)");
                    stmt.run(name, age, department, place);
                    stmt.finalize();

                    db.each("SELECT * FROM Employees", (err, row) => {
                        if (err) {
                            console.error(err.message);
                        }
                        console.log(row);
                    });
                });
                db.close();
                rl.close();
            });
        });
    });
});
