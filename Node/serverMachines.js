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

app.get('/machines', function (req, res) {
	console.log(token) ;
	if ( token == "" ) {
	  res.render('vra-logon', {vraData: null, error: null});
	}
	else {
		getPayload(token, res) ;
	}
})

let host = "us08-1-vralb.oc.vmware.com"
let tenant = "cava"

function getPayload (token, res) {

  let request = "" ;

  // the get options
  optionsget = {
      host : host,
      path : '/catalog-service/api/consumer/resourceViews?&withExtendedData=true&withOperations=true&limit=5000',
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


	let m = [] ;

	hres.on('end', () => {

		r = JSON.parse(request) ;
		
		console.log(r)

		r["content"].forEach((v) => {
			console.log(v['name'],v['status']) ;
		});

		r["content"].forEach((v)  => {
			if ( v['resourceType'] == "Infrastructure.Virtual" ) {
				m.push(v)
			}
		}) ;
		res.render('index2',{requests: m});

	});

  });
  
  res1.write('')
  res1.end()

}

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
 
let token = "" ;
let tokenData = "" ;


app.post('/', function (req, res) {

  console.log(token);
 
  if ( token != "" ) {

	getPayload(token, res) ;
  }
  else {
  let username = req.body.username;
  let password = req.body.password;

  logonJson = JSON.stringify({
    "username" : username,
    "password" : password,
    "tenant" : tenant,
  });

  // prepare the header
  postheaders = {
      'Content-Type' : 'application/json',
      'Content-Length' : Buffer.byteLength(logonJson, 'utf8')
  };
 
  // the post options
  optionspost = {
      host : host,
      port : 443,
      path : '/identity/api/tokens',
      method : 'POST',
      rejectUnauthorized: false,
      headers : postheaders
  };

  //res.render('vra-logon', {vraData: "test", error: null});
  
  logon = https.request(optionspost, function getToken(hres) {

    hres.on('data', function(d) {
	    tokenData += d ;
    });

    hres.on('end', function(d) {
	token = JSON.parse(tokenData)["id"]
	expires = JSON.parse(tokenData)["expires"]
	console.log(token);
	console.log(expires);

        //res.render('vra-logon', {vraData: expires, error: null});

	getPayload(token, res) ;

    });

  });

  logon.write(logonJson);
  logon.end()
  }

})


app.post('/machines', function (req, res) {

  console.log(token);
 
  if ( token != "" ) {
	getPayload(token, res) ;
  }

})


