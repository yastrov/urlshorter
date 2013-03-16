function newUrl(url, text) {
    var new_url = document.createElement('a');
    new_url.setAttribute('href', url);
    new_url.innerHTML= text;
    return new_url
}

function newContainer() {
    var container = document.createElement('p');
    container.id = 'url-info';
    container.className = 'textcenter';
    var div = document.getElementById("content");
    div.appendChild(container);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$( document ).ready(function() {
    $("form").submit(function() {
        sendAjax();
        return false;
    });
    newContainer();
});

function sendAjax(){
$.ajax({
    type: "POST",
    contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
    url: "/create/",
    data: $('form').serialize(),
    beforeSend: function ( xhr, settings ) {
        var myRe = /https?:\/\/\w+/ig;
        var v = $("input[name='url']").val();
        if ( !myRe.test(v) ) {
            $( "#url-info" ).html("<strong>Bad url</strong>");
            return false;
        }
        if (!csrfSafeMethod(settings.type)) {
            var csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
}).done(function(data) {
    var div = document.getElementById("url-info");
    div.innerHTML = "Url: "
    div.appendChild(newUrl(data.short, data.short) );
}).fail(function() {
    alert("error"); 
    console.log("Ajax fail");
});
}
