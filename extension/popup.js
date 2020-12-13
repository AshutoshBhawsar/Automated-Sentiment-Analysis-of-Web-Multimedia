
// Helper function to create CORS Request
function createCORSRequest(method, url) {
	  var xhr = new XMLHttpRequest();
	  if ("withCredentials" in xhr) {
		// XHR for Chrome/Firefox/Opera/Safari.
		xhr.open(method, url, true);
	  } else if (typeof XDomainRequest != "undefined") {
		// XDomainRequest for IE.
		xhr = new XDomainRequest();
		xhr.open(method, url);
	  } else {
		// CORS not supported.
		xhr = null;
	  }
	return xhr;
}

// Function to check if returned value by server is result or not and displays it on html
function isResult(text)
{
	var flag = 0;
	var emo = "";

	if((text.indexOf("trust") != -1) || (text.indexOf("love") != -1) || (text.indexOf("joy") != -1) || (text.indexOf("anger") != -1) || (text.indexOf("surprise") != -1) || (text.indexOf("sadness") != -1) || (text.indexOf("disgust") != -1) || (text.indexOf("fear") != -1))
	{
		flag = 1;
	}
	if (flag == 1)
	{
		var res = text.split(",");
		var i;
		for(i=0;i<3;i=i+1)
		{
			if (res[i].indexOf("trust") != -1)
			{
				emo = emo + "\nTrust: " + String.fromCodePoint(0x1F607);
			}
			else if (res[i].indexOf("love") != -1)
			{
				emo = emo + "\nLove: " + String.fromCodePoint(0x2764);
			}
			else if (res[i].indexOf("joy") != -1)
			{
				emo = emo + "\nJoy: " + String.fromCodePoint(0x1F604);
			}
			else if (res[i].indexOf("anger") != -1)
			{
				emo = emo + "\nAnger: " + String.fromCodePoint(0x1F620);
			}
			else if (res[i].indexOf("surprise") != -1)
			{
				emo = emo + "\nSurprise: " + String.fromCodePoint(0x1F62F);
			}
			else if (res[i].indexOf("sadness") != -1)
			{
				emo = emo + "\nSadness: " + String.fromCodePoint(0x1F614);
			}
			else if (res[i].indexOf("disgust") != -1)
			{
				emo = emo + "\nDisgust: " + String.fromCodePoint(0x1F922);
			}
			else if (res[i].indexOf("fear") != -1)
			{
				emo = emo + "\nFear: " + String.fromCodePoint(0x1F628);
			}
		}
	}
	document.getElementById('revert2').innerHTML=emo;
	return emo;
}

// Actual CORS request.
function makeCorsRequest(tablink) {

	  var url = 'http://localhost/extension/php_connector.php';

	  var xhr = createCORSRequest('POST', url);
	  if (!xhr) {
		document.getElementById('revert').innerHTML = 'CORS not supported';
		return;
	  }

	  // Response handlers.
	  xhr.onload = function() {
		var text = xhr.responseText;
		var emo = "";

		emo = isResult(text);
		/*
		if (text.indexOf("trust") != -1)
		{
			emo = emo + "\nTrust: " + String.fromCodePoint(0x1F607);
		}
		if (text.indexOf("love") != -1)
		{
			emo = emo + "\nLove: " + String.fromCodePoint(0x2764);
		}
		if (text.indexOf("joy") != -1)
		{
			emo = emo + "\nJoy: " + String.fromCodePoint(0x1F604);
		}
		if (text.indexOf("anger") != -1)
		{
			emo = emo + "\nAnger: " + String.fromCodePoint(0x1F620);
		}
		if (text.indexOf("surprise") != -1)
		{
			emo = emo + "\nSurprise: " + String.fromCodePoint(0x1F62F);
		}
		if (text.indexOf("sadness") != -1)
		{
			emo = emo + "\nSadness: " + String.fromCodePoint(0x1F614);
		}
		if (text.indexOf("disgust") != -1)
		{
			emo = emo + "\nDisgust: " + String.fromCodePoint(0x1F922);
		}
		if (text.indexOf("fear") != -1)
		{
			emo = emo + "\nFear: " + String.fromCodePoint(0x1F628);
		}
		*/
		text = "The media contains";
		document.getElementById('revert').innerHTML=text;
		//document.getElementById('revert2').innerHTML=emo;
	  };

	  xhr.onerror = function() {
		document.getElementById('revert').innerHTML = 'Woops, there was an error making the request.';
	  };
	  var str = "url="+String(tablink);
	  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	  xhr.send(str);
	  document.getElementById('revert').innerHTML = 'Contacting server...';
}

function transfer(){
	var tablink;
	chrome.tabs.getSelected(null, function(tab) {
	   	tablink = tab.url;
		tablink = tablink.replace("https","http");
			if(tablink.indexOf("youtube") != -1)
			{
				if (tablink.indexOf("list")!=-1)
				{
					document.getElementById('revert').innerHTML = 'You are watching video from playlist. Playlists are not supported.';
					return;
				}
				else if(tablink.indexOf("watch")!=-1)
				{
					var a = makeCorsRequest;
					a(tablink);
					return;
				}
				else
				{
					document.getElementById('revert').innerHTML = 'You have not opened any multimedia page. Please open page containing multimedia.';
					return;
				}
			}
			else
			{
				document.getElementById('revert').innerHTML = 'You have not opened any multimedia page. Please open page containing multimedia.';
				return;
			}
	});

	return;
}

$(document).ready(function(){
    $("button").click(function(){

		var b = transfer();
		//document.getElementById('revert').innerHTML = 'Contacting Server'+b;

		//var a = makeCorsRequest;
		//a(b);

    });
});
