// var req;
// 	function sendRequest()
// 	{
// 		console.log("Sending request")
// 		req = new XMLHttpRequest();
// 		req.onreadystatechange = handleResponse;
// 		req.open("GET","/first",true);
// 		req.send(null);
// 	}
// 	function handleResponse()
// 	{
// 		if(req.readyState == 4 && req.status == 200)
// 		{
// 			console.log("readyState changed")
// 			var response = req.responseText;
// 			document.getElementById("div1").innerHTML=response;

// 		}
// 	}
// 	function init()
// 	{

//  	console.log("stop here")
// 	document.getElementById("btnSendRequest").onclick=sendRequest;
//  	return false;
//  	}

 	var req;
	function sendRequest()
	{
		req = new XMLHttpRequest();
		req.onreadystatechange = handleResponse;
		req.open("GET","/first",true);
		req.send(null);
	}
	function handleResponse()
{
	if(req.readyState==4&&req.status==200){
	var response=req.responseText;
	var content="<table border=2><tr><td>Bus Number</td><td>Start Point</td><td>End Point</td><td>Route Info</td>"
	var busArray=response.getElementsByTagName("BusRouteInfo");
	for(var i=0;i<busArray.length;i++){
		content+="<tr>"
		content+="<td>"
		content+=busArray[i].getElementsByTagName("no")[0].childNodes[0].nodeValue;
		content+="</td>";
		content+="<td>";
		content+=busArray[i].getElementsByTagName("start_point")[0].childNodes[0].nodeValue;
		content+="</td>";
		content+="<td>";
		content+=busArray[i].getElementsByTagName("End_point")[0].childNodes[0].nodeValue;
		content+="</td>";
		content+="<td>";
		content+=busArray[i].getElementsByTagName("route")[0].childNodes[0].nodeValue;
		content+="</td>";
		content+="</tr>";
	}
	content+="</table>";
	document.getElementById("div1").innerHTML=content;
	}	
}
	function init()
	{

 	console.log("stop here")
	document.getElementById("btnSendRequest").onclick=sendRequest;
 	return false;
 	}