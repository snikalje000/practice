(function ($) {
	"use strict";

	$(window).stellar({
		responsive: true,
		parallaxBackgrounds: true,
		parallaxElements: true,
		horizontalScrolling: false,
		hideDistantElements: false,
		scrollProperty: "scroll",
	});

	var fullHeight = function () {
		$(".js-fullheight").css("height", $(window).height());
		$(window).resize(function () {
			$(".js-fullheight").css("height", $(window).height());
		});
	};
	fullHeight();

	// loader
	 var loader = function () {
	 	setTimeout(function () {
	 		if ($("#ftco-loader").length > 0) {
	 			$("#ftco-loader").removeClass("show");
	 		}
	 	}, 1);
	 };
	 loader();



	// Scrollax
	$.Scrollax();

	var carousel = function () {
		$(".carousel-testimony").owlCarousel({
			center: false,
			loop: true,
			items: 1,
			margin: 30,
			stagePadding: 0,
			nav: false,
			navText: [
				'<span class="ion-ios-arrow-back">',
				'<span class="ion-ios-arrow-forward">',
			],
			responsive: {
				0: {
					items: 1,
					autoplay: false, // Disable autoplay on screens smaller than 600 pixels
				},
				600: {
					items: 2,
					autoplay: false,
					autoplayTimeout: 3000,
				},
				1000: {
					items: 4,
					autoplay: true,
					autoplayTimeout: 3000,
				},
			},
		});
	};

	carousel();

	//   testimonial about
	// Scrollax
	$.Scrollax();

	var carousel = function () {
		$(".carousel-testimony1").owlCarousel({
			center: false,
			loop: false,
			items: 1,
			margin: 30,
			stagePadding: 0,
			nav: false,
			navText: [
				'<span class="ion-ios-arrow-back">',
				'<span class="ion-ios-arrow-forward">',
			],
			responsive: {
				0: {
					items: 1,
					autoplay: false, // Disable autoplay on screens smaller than 600 pixels
				},
				600: {
					items: 2,
					autoplay: false,
					autoplayTimeout: 3000,
				},
				1000: {
					items: 4,
					autoplay: false,
					autoplayTimeout: 3000,
				},
			},
		});
	};

	carousel();

	$("nav .dropdown").hover(
		function () {
			var $this = $(this);
			// 	 timer;
			// clearTimeout(timer);
			$this.addClass("show");
			$this.find("> a").attr("aria-expanded", true);
			// $this.find('.dropdown-menu').addClass('animated-fast fadeInUp show');
			$this.find(".dropdown-menu").addClass("show");
		},
		function () {
			var $this = $(this);
			// timer;
			// timer = setTimeout(function(){
			$this.removeClass("show");
			$this.find("> a").attr("aria-expanded", false);
			// $this.find('.dropdown-menu').removeClass('animated-fast fadeInUp show');
			$this.find(".dropdown-menu").removeClass("show");
			// }, 100);
		}
	);

	$("#dropdown04").on("show.bs.dropdown", function () {
		console.log("show");
	});

	// scroll
	var scrollWindow = function () {
		$(window).scroll(function () {
			var $w = $(this),
				st = $w.scrollTop(),
				navbar = $(".ftco_navbar"),
				sd = $(".js-scroll-wrap");

			if (st > 150) {
				if (!navbar.hasClass("scrolled")) {
					navbar.addClass("scrolled");
				}
			}
			if (st < 150) {
				if (navbar.hasClass("scrolled")) {
					navbar.removeClass("scrolled sleep");
				}
			}
			if (st > 350) {
				if (!navbar.hasClass("awake")) {
					navbar.addClass("awake");
				}

				if (sd.length > 0) {
					sd.addClass("sleep");
				}
			}
			if (st < 350) {
				if (navbar.hasClass("awake")) {
					navbar.removeClass("awake");
					navbar.addClass("sleep");
				}
				if (sd.length > 0) {
					sd.removeClass("sleep");
				}
			}
		});
	};
	scrollWindow();

	var isMobile = {
		Android: function () {
			return navigator.userAgent.match(/Android/i);
		},
		BlackBerry: function () {
			return navigator.userAgent.match(/BlackBerry/i);
		},
		iOS: function () {
			return navigator.userAgent.match(/iPhone|iPad|iPod/i);
		},
		Opera: function () {
			return navigator.userAgent.match(/Opera Mini/i);
		},
		Windows: function () {
			return navigator.userAgent.match(/IEMobile/i);
		},
		any: function () {
			return (
				isMobile.Android() ||
				isMobile.BlackBerry() ||
				isMobile.iOS() ||
				isMobile.Opera() ||
				isMobile.Windows()
			);
		},
	};

	// counter();
	var counter = function () {
		$("#section-counter, .hero-wrap, .ftco-counter").waypoint(
			function (direction) {
				if (
					direction === "down" &&
					!$(this.element).hasClass("ftco-animated")
				) {
					var comma_separator_number_step =
						$.animateNumber.numberStepFactories.separator(",");
					$(".number").each(function () {
						var $this = $(this),
							num = $this.data("number");
						$this.animateNumber(
							{
								number: num,
								numberStep: function (now, tween) {
									var formatted;
									if (num === 200 || num === 400) {
										formatted = Math.floor(now).toLocaleString() + "+";
									} else if (num === 62 || num === 85) {
										formatted = Math.floor(now).toLocaleString() + "%";
									} else {
										formatted = Math.floor(now).toLocaleString();
									}
									$this.text(formatted);
									// Stop animation when current value reaches the target value
									if (now >= num) {
										$this.stop(tween);
									}
								},
							},
							7000
						);
					});
				}
			},
			{ offset: "95%" }
		);
	};

	counter();

	var contentWayPoint = function () {
		var i = 0;
		$(".ftco-animate").waypoint(
			function (direction) {
				if (
					direction === "down" &&
					!$(this.element).hasClass("ftco-animated")
				) {
					i++;

					$(this.element).addClass("item-animate");
					setTimeout(function () {
						$("body .ftco-animate.item-animate").each(function (k) {
							var el = $(this);
							setTimeout(
								function () {
									var effect = el.data("animate-effect");
									if (effect === "fadeIn") {
										el.addClass("fadeIn ftco-animated");
									} else if (effect === "fadeInLeft") {
										el.addClass("fadeInLeft ftco-animated");
									} else if (effect === "fadeInRight") {
										el.addClass("fadeInRight ftco-animated");
									} else {
										el.addClass("fadeInUp ftco-animated");
									}
									el.removeClass("item-animate");
								},
								k * 50,
								"easeInOutExpo"
							);
						});
					}, 100);
				}
			},
			{ offset: "95%" }
		);
	};
	contentWayPoint();
	
// Vanilla JavaScript
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
	anchor.addEventListener("click", function (e) {
		e.preventDefault();

		document.querySelector(this.getAttribute("href")).scrollIntoView({
			behavior: "smooth",
		});
	});
});


	// video
	$(document).ready(function () {
		// get video source from data-src button
		var $videoSrc;
		$(".video-btn").click(function () {
			$videoSrc = $(this).data("src");
		});
		console.log($videoSrc);
		// autoplay video on modal load
		$("#exampleModal").on("shown.bs.modal", function (e) {
			// youtube iframe configuration and settings
			$("#video").attr(
				"src",
				$videoSrc + "?autoplay=1&rel=0&controls=1&loop=1&modestbranding=1"
			);
		});
		// stop playing the youtube video when modal closed
		$("#exampleModal").on("hide.bs.modal", function (e) {
			// stop video
			$("#video").attr("src", $videoSrc);
		});
	});

	// custom

	
})(jQuery);
