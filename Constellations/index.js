const express = require("express");
const app = express();

app.listen(3001, () => console.log("Hola Selfie App!"))
app.use(express.static("public"))