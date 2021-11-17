function clickLogin() {


      $("#LOGINFORM").on("click","#LOGINSUBMIT",function(){
        console.log('login submit clicked')
        let loginUsername = $("#loginUsername").val()
        console.log("loginUsername:",loginUsername)
        let loginPasswd = $("#loginPasswd").val()
        console.log("loginPasswd:",loginPasswd)
      

        let passJSON = {"userName":loginUsername,"passWd":loginPasswd}
        authentication(passJSON)
        // $("#CLOSEBUTTON").click()
      });
}

function authentication(passJSON){
    console.log(passJSON)
    $.ajax({
        "url":"/loginInfo/",
        "type":"get",
        "datatype":"json",
        success:function(result){
            compare(passJSON,result)
        },
        error:function(e){
            console.log("error happened")
        }
    })
}

function compare(passJSON,result){
    
    let flag = 0;
    for (value of result){
        if (passJSON.userName == value.userName && passJSON.passWd == value.passWd){
            flag = 1;
            break;
        }
    }
    if(flag == 1){
        $(location).attr('href', '/indexPage/');
        
    }else{
        alert("account does not exist")
    }
}

// function clickLoginSubmit(){
//     $('#LOGINSUBMIT').bind('click',function(){
//         console.log('login submit clicked')
//     }
// }
