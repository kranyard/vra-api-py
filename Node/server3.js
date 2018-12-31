const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const https = require('https');
 
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));
app.set('view engine', 'ejs')

app.get('/', function (req, res) {
  res.render('vra-logon', {weather: null, error: null});
})


app.post('/', function (req, res) {
  let username = req.body.username;
  let password = req.body.password;

  jsonObject = JSON.stringify({
    "username" : username,
    "password" : password,
    "tenant" : "vsphere.local"
  });

  // prepare the header
  postheaders = {
      'Content-Type' : 'application/json',
      'Content-Length' : Buffer.byteLength(jsonObject, 'utf8')
  };
 
  // the post options
  optionspost = {
      host : 'vra-01a.corp.local',
      port : 443,
      path : '/identity/api/tokens',
      method : 'POST',
      rejectUnauthorized: false,
      headers : postheaders
  };

  //res.render('vra-logon', {weather: "test", error: null});
  

  h = https.request(optionspost, function(hres) {
    console.log("statusCode: ", res.statusCode);
    // uncomment it for header details
    console.log("headers: ", res.headers);

    hres.on('data', function(d) {
        console.info('POST result:\n');
        process.stdout.write(d);
        res.render('vra-logon', {weather: d, error: null});
        console.info('\n\nPOST completed');
    });
  });
  h.write(jsonObject);
  h.end()
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
 
