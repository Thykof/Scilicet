
$(document).ready(function(){

  // Submit post on submit
  $('#post-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check
      create_post();
  });

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });

  function create_post() {
    console.log("create post is working!") // sanity check
    url_action = $('#post-form').attr('action');
    console.log(url_action);
    $.ajax({
        url : url_action, // the endpoint
        type : "POST", // http method
        data : { category_name : $('#id_name').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#id_name').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            $("#results").prepend("<p><strong>"+json.text+"</strong> - <em> "+json.author+"</em></p>");
            console.log("success"); // another sanity check
            $("#form-category").modal("hide");
            var last_id = $('#id_category option').last().val()
            $("#id_category").append(new Option(json.text, last_id+1));
            $("#id_category").val(last_id+1);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html('<div class="alert-box alert radius" data-alert>Ho zut ! une erreur est survenue : ' +
            errmsg + ' <a href=""#" class="close">&times;</a></div>'); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });

  }


})
