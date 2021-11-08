function clickLogin() {
    $("#LOGINLINK").click(function(){
        console.log('Login link was clicked');
        $("#LOGINFORM").html(("<div class='login-box' >"+
            "<button id = 'CLOSEBUTTON' class='status incorrect'></button>"+
            "<span>FlowTow</span>"+
        
            "<div>"+
            "<div class='input-content'>"+
                "<div>"+
                "<input id = 'username' type='text' autocomplete='off' placeholder='user name' />"+
                "</div>"+
                "<div>"+
                "<input id = 'passwd' type='password' autocomplete='off' placeholder='pass word'  />"+
                "</div>"+
            "</div>"+
            "<div class='button-b'>"+
            "<button id = 'LOGINSUBMIT' type='submit' class='enter-btn'>submit</button>"+
            "</div>"+
            "</div>"+

        
        "</div>"))
    });

    $("#LOGINFORM").on("click","#CLOSEBUTTON",function(){
        $("#LOGINFORM").empty()
      });
}

function clickLoginSubmit(){
    
}
