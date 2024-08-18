const trailer = document.getElementById("trailer");

const animateTrailer = (e, interacting) => {
	const x = e.clientX - trailer.offsetWidth / 2;
	const y = e.clientY - trailer.offsetHeight / 2;

	const keyframes = {
		transform: `translate(${x}px, ${y}px) scale(${interacting ? 0 : 1})`,
	};

	trailer.animate(keyframes, {
		duration: 800,
		fill: "forwards",
	});
};

const checkIfMouseInInteractable = (e) => {
	const interactable = document.querySelector(".interactable");
	let interacting = false;

	const rect = interactable.getBoundingClientRect();
	const mouseX = e.clientX;
	const mouseY = e.clientY;

	if (
		mouseX >= rect.left &&
		mouseX <= rect.right &&
		mouseY >= rect.top &&
		mouseY <= rect.bottom
	) {
		interacting = true;
	}

	return interacting;
};

window.onmousemove = (e) => {
	const interacting = checkIfMouseInInteractable(e);
	animateTrailer(e, interacting);
};
