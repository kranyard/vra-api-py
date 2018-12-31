const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const https = require('https');
 
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));
app.set('view engine', 'ejs')

app.get('/', function (req, res) {
  res.render('vra-logon', {vraData: null, error: null});
})

function getPayload (token, res) {

  let request = "" ;

  // the get options
  optionsget = {
      host : 'vra-01a.corp.local',
      path : '/catalog-service/api/consumer/requests?limit=30&$orderby=requestNumber%20desc',
      method : 'GET',
      rejectUnauthorized: false,
      headers : {
	      'Accept':'application/json;charset=UTF-8',
	      'Content-Type' : 'application/json',
	      'Authorization' : 'Bearer '+token
      }
  };

  res1 = https.request(optionsget, function(hres) {


	hres.on('data', function(d) {
		request += d 
    	});


	hres.on('end', () => {

		r = JSON.parse(request) ;

		console.log(res)
		res.render('index1',{requests: r["content"]});
		r["content"].forEach((v) => {
			console.log(v['id'],v['requestNumber'],v['phase'],v['@type']) ;
		});

	});

  });
  
  res1.write('')
  res1.end()

}

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
 

app.post('/', function (req, res) {
  let username = req.body.username;
  let password = req.body.password;

  logonJson = JSON.stringify({
    "username" : username,
    "password" : password,
    "tenant" : "vsphere.local"
  });

  // prepare the header
  postheaders = {
      'Content-Type' : 'application/json',
      'Content-Length' : Buffer.byteLength(logonJson, 'utf8')
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

  //res.render('vra-logon', {vraData: "test", error: null});
  
  let token = "" ;
  let tokenData = "" ;

  logon = https.request(optionspost, function getToken(hres) {

    hres.on('data', function(d) {
	    tokenData += d ;
    });

    hres.on('end', function(d) {
	token = JSON.parse(tokenData)["id"]
	expires = JSON.parse(tokenData)["expires"]

        //res.render('vra-logon', {vraData: expires, error: null});

	getPayload(token, res) ;

    });

  });

  logon.write(logonJson);
  logon.end()

})


