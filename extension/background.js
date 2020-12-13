chrome.runtime.onMessage.addListener(function(request, sender, callback) {if (request.action == "xhttp") {    $.ajax({
    type: request.method,
    url: request.url,
    data: request.data,
    success: function(responseText){
        callback(responseText);
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
        callback();
    }
});

return true; }});