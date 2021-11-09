function clickRegister() {
    $("#REGISTERLINK").click(function(){
        console.log('register clicked')
        $("#REGISTERFORM").html(("<div class='login-box' >"+
            "<button id = 'CLOSEBUTTON' class='status incorrect'></button>"+
            "<span>Register</span>"+
        
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

      $("#REGISTERFORM").on("click","#REGISTERSUBMIT",function(){
        console.log("register submite was clicked")
        let registerUsername = $("#registerUsername").val()
        console.log("registerUsername:",registerUsername)
        let registerPasswd = $("#registerPasswd").val()
        console.log("registerPasswd:",registerPasswd)
        let registerEmail = $("#registerEmail").val()
        console.log("registerEmail:",registerEmail)
        let main_root = '127.0.0.1:8000/'
        $.ajax({
            url:"/loginInfo/",
            data:{"userName":registerUsername,
            "passWd":registerPasswd,
            "email":registerEmail},
            type:"post",
            datatype:"json",
            success:function(result){
                alert("register successfully,you can log in")
                $("#CLOSEBUTTON").click()
                $("#LOGINLINK").click()
            },
            error:function(e){
                console.log('register failed')
            }

        })

      });
};

function checkEmail(email)
{
    email = email.toLowerCase();
    if (/^[a-z0-9]{1}[a-z0-9_-]{1,}@[a-z0-9]{1,}(\.[a-z]{2,})*\.[a-z]{2,}$/.test(email)) {
        return 1;
    } else {
        return 0;
    }
}



