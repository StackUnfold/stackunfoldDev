
var userRegistrations = {

    init: function(){
        userRegistrations.signUp();
    },

    getInputValues: () => {

        var username = $('#username').val();
        var user_email = $('#user-email').val();
        var user_password = $('#user-password').val();

        return {'username': username, 'user_email':user_email, 'user_password':user_password};

    },

    signUp: () => {

        $('.sign_up').click(function(){
            var user_details = userRegistrations.getInputValues();
            alert(user_details);
        })
    }



}


