$("form").submit(function (e) {
    e.preventDefault();
    var formId = this.id;  // "this" is a reference to the submitted form
    var username = $('#username').value
    var password = $('#password').value
    
    console.log(username, password)
});