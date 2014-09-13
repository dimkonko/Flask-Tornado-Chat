window.onload = function() {
	
	$("#firstLine").fadeTo(0, 1, function() {
		$("#secondLine").fadeTo(0, 1, function() {
			$("#menubar").fadeTo(0, 1);
		})
	});

	var loginBut = document.getElementById("login_but");
		signupBut = document.getElementById("signup_but");

	var loginModal = new Modal(document.getElementById("login_modal")),
		signupModal = new Modal(document.getElementById("signup_modal"))
		

	loginBut.onclick = function() {
		loginModal.show();
	};

	signupBut.onclick = function() {
		signupModal.show();
	};
}