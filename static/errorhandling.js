// $('#fullname').blur(function() {
//     var fullname = $('#fullname').val();
//     var fullnameCount = $('#fullname').val().length;
//     console.log(fullnameCount);
//     if(fullnameCount < 5){
//         $('#error-fullname').show();
//         $('#error-fullname').html("*Email must be at least 5 characters long");
//         console.log("name must be at least 5 character");
//     }
//     else {
//         $('#error-fullname').hide();
//     }
//     if(fullname != "[a-zA-Z0-9]") {
//     $('#error-fullname').html("*Email must be alphanumeric");
//         $('#error-fullname').show();
//         console.log("must be alphanumeric");
//     }
//     else {
//         $('#error-fullname').hide();
//     }
// });


//copied code from my codepen project where i will implement the same functions for this project


// var username;
// var usernameCount;
// var password;
// var ck_username = /^[A-z]+$/;

// //hide error divs
// $('.error').hide();


// $('#username').keyup(function() {
//     usernameCount = $('#username').val().length;
//     username = $('#username').val();
//     //alert(usernameCount);
//     if(usernameCount < 2){
//         $('#username-error').show().html("Username is too short");      
//     }
//     else if (!ck_username.test(username)) {
//         $('#username-error').show().html("Username must be a-z");
//     }
//     else {
//         $("#username-error").hide();
//     }
// });


// //can use blur instead of keyup to check once user has left textbox instead of when they type

// $('#password').keyup(function() {
//     password = $("#password").val().length;
//     if(password < 2) {
//         $('#password-error').show().html("Password is too short");
//     }
//     else {
//         $('#password-error').hide();
//     }
// })

