$(document).ready(function(){
//添加文章
$("#addArticle").click(function(){
	var title = $("#artTitle").val();
	var content = $("#artContent").val();
	$.ajax({
		type: "post",
		url: "/admin/add",
		data: {
			"title": title,
			"content": content
		},
		success: function(){
			alert("添加成功");
		}
	});
});

//删除文章
$(".listArticle").on("click","input",function(){
    var obj = $(this)
	var id= obj.prev().attr("id");
	alert(id);
	$.ajax({
        type: "post",
        url: "/admin/list",
        data: {
            "cmd": "delArticle",
            "id": id
        },
        success: function(){
            obj.parent().hide(500);
        },
    });
});

//检查用户名是否存在
$("#username").blur(function(){
	var username = $("#username").val();
	$.ajax({
		type: "post",
		url: "/admin/login",
		data: {"username": username},
		success: function(msg){
			if(msg == "1"){
				alert("此用户不存在!!!");
			}/*else if(msg == "0"){
				alert("此用户存在!!!");	
			}*/	
		}
	});
});

//登录
$("#login").click(function(){
	var username = $("#username").val();
	var password = $("#password").val();
	$.ajax({
		type: "post",
		url: "/admin/login",
		data: {
			"username": username,
			"password": password
		},
		success: function(msg){
			if(msg == "0"){
				alert("登录成功");
				window.location.href="/";
			}else if(msg == "-1"){
				alert("密码错误");	
			}	
		}
	});
});

});
