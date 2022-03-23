var express = require('express');
var app = express();
var url = "mongodb://mongo:27017/nginx";
var MongoClient = require('mongodb').MongoClient;

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  console.log("Database created!");
  db.close();
});

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbase = db.db("nginx");
    console.log("Switched to "+db.databaseName+" database");
    dbase.createCollection("access", function(err, result) {
        if (err) throw err;
        console.log("Collection is created!");
        db.close();
    });
});


app.get('/', function(req, res) {
  res.send('Hello from E-Bot7');
});

var port = process.env.PORT;
app.listen(port);
console.log('Listening on localhost:'+ port);
