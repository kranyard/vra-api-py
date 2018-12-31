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

  // the get options
  optionsget = {
      host : 'vra-01a.corp.local',
      port : 443,
      path : '/catalog-service/api/consumer/entitledCatalogItemViews',
      method : 'GET',
      headers : {
	      'Accept':'application/json;charset=UTF-8',
	      'Content-Type' : 'application/json',
	      'Authorization' : 'Bearer {token}'
      }
  };

  //res.render('vra-logon', {weather: "test", error: null});
  

  h = https.request(optionspost, function(hres) {
    console.log("statusCode: ", res.statusCode);
    // uncomment it for header details
    console.log("headers: ", res.headers);

    hres.on('data', function(d) {
        console.info('POST result:\n');
        process.stdout.write(d);
	j = JSON.parse(d)
	token = j["id"];
        process.stdout.write(token);
        res.render('vra-logon', {weather: d, error: null});
        console.info('\n\nPOST completed');
    });
  });
  h.write(jsonObject);
  h.end()

  x = https.request(optionsget, function(hres) {
    hres.on('data', function(d) {
	process.stdout.write(d)
    });
  });
  
  x.write()

  x.end()

})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
 
