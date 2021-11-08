function clickRegister() {
    $("#REGISTERLINK").click(function(){
        console.log('Login link was clicked');
        $("#REGISTERFORM").html(("<div class='login-box' >"+
            "<button id = 'CLOSEBUTTON' class='status incorrect'></button>"+
            "<span>FlowTow</span>"+
        
            "<div>"+
            "<div class='input-content'>"+
                "<div>"+
                "<input id = 'registerUsername' type='text' autocomplete='off' placeholder='user name' />"+
                "</div>"+
                "<div>"+
                "<input id = 'registerPasswd' type='password' autocomplete='off' placeholder='pass word'  />"+
                "</div>"+
                "<input id = 'registerEmail' type='password' autocomplete='off' placeholder='email'  />"+
                "</div>"+
            "</div>"+
            "<div class='button-rb'>"+
            "<button id = 'REGISTERSUBMIT' type='submit' class='enter-btn'>submit</button>"+
            "</div>"+
            "</div>"+

        
        "</div>"))
    });

    $("#REGISTERFORM").on("click","#CLOSEBUTTON",function(){
        $("#REGISTERFORM").empty()
      });
}
function clickLoginSubmit(){
    $("#REGISTERSUBMIT").on("click","#LOGINSUBMIT",function(){
        let username = $('#registerUsername').val();
        console.log(username);

    });
      
}
