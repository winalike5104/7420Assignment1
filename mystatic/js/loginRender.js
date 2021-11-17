const renderLogin = () =>{
    
    $("#LOGINFORM").html(("<div class='login-box' >"+
        "<button id = 'CLOSEBUTTON' class='status incorrect'></button>"+
        "<span>Login</span>"+
    
        "<div>"+
            "<div class='input-content'>"+
                "<div>"+
                "<input id = 'loginUsername' type='text' autocomplete='off' placeholder='user name' />"+
                "</div>"+
                "<div>"+
                "<input id = 'loginPasswd' type='password' autocomplete='off' placeholder='pass word'  />"+
                "</div>"+
            "</div>"+
            "<div class='button-b'>"+
                "<button id = 'LOGINSUBMIT' type='submit' class='enter-btn'>submit</button>"+
            "</div>"+
    
        "</div>"+
        

    
    "</div>"));
        
}