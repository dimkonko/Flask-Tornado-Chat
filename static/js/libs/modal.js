var Modal = function(modalDiv) {
	var isModalOpen = false;

	function init() {
		var wrapperDiv = document.createElement("div");
		var parent = modalDiv.parentNode;
		wrapperDiv.setAttribute("id", "main_modal");
		wrapperDiv.setAttribute("class", "modal_wrapper");
		wrapperDiv.appendChild(modalDiv);
		parent.appendChild(wrapperDiv);
		return wrapperDiv;
	}

	function show() {
		/*
		 * Openes the modal window
		 */
		modalDiv.style.visibility = "visible";
		isModalOpen = true;
	}

	function close(event) {
		/*
		 * Closing modal when clicked outside the modal window
		 */
		if(event.target.id == "main_modal" && isModalOpen) {
			modalDiv.style.visibility = "hidden";
			isModalOpen = false;
		}
	}

	modalDiv = init();
	modalDiv.onclick = function(event) {
		close(event);
	}

	return {
		show: show,
		close: close
	}
}