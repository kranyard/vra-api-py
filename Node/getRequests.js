const https = require('https');
 
loginJson = JSON.stringify({
	"username" : "jason@corp.local",
	"password" : "VMware1!",
	"tenant" : "vsphere.local"
});

// prepare the header
postheaders = {
      'Content-Type' : 'application/json',
      'Content-Length' : Buffer.byteLength(loginJson, 'utf8')
};

// the post options
optionspost = {
      host : 'vra-01a.corp.local',
      path : '/identity/api/tokens',
      method : 'POST',
      rejectUnauthorized: false,
      headers : postheaders
};

h = https.request(optionspost, function(hres) {

    hres.on('data', getRequests)

    hres.on('end', () => {

	console.log(token)

    }) ;

});


let request = "" ;
let token = "" ;

function getRequests(res) {
	j = JSON.parse(res)
	token = j["id"]

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

		r["content"].forEach((v) => {
			console.log(v['id'],v['requestNumber'],v['phase'],v['@type']) ;
		});

	});

  });
  
  res1.write('')
  res1.end()

}

h.write(loginJson);
h.end();
