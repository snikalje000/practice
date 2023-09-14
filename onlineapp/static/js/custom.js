$(document).ready(function () {
    // Check if the popup has been shown before using local storage
    var isFormSubmitted = localStorage.getItem('isFormSubmitted') === 'true';
    var serverReceivedData = false; // Assume the server has not received data initially

    function showPopup() {
      // Skip showing the popup if the form has been submitted or if the server received data
      if (!isFormSubmitted && !serverReceivedData) {
        $("#once-popup").fadeIn();
      }
    }

    function resetPopupTimer() {
      setTimeout(function () {
        showPopup();
        resetPopupTimer();
      }, 300000); // Show the popup every 30 seconds (30000 milliseconds)
    }

    // Start showing the popup after 2000 milliseconds (2 seconds)
    setTimeout(function () {
      showPopup();
      resetPopupTimer();
    }, 10000);

    $('.sid1, .sid2').click(function () {
      $('#once-popup').hide();
    });

    $('#popup-close').click(function () {
      $('#once-popup').fadeOut();
      resetPopupTimer(); // Restart the timer after the popup is dismissed
    });

    $('#connect-btn').click(function (e) {
      e.preventDefault(); 
      var mobileNumber = $('#mobile-input').val();
      console.log('Mobile Number:', mobileNumber);

      var mobileNumberRegex = /^\d{10}$/; 
      if (mobileNumberRegex.test(mobileNumber)) {
      
        console.log('Valid mobile number!');
        $('#mobile-input').css('border-color', 'green');
        localStorage.setItem('isFormSubmitted', 'true');
        setTimeout(function () {
          serverReceivedData = true;
        }, 1000);
        $("#once-popup").fadeOut();
        resetPopupTimer();
        $('#popup-form').submit();
      } else {
        console.log('Invalid mobile number! Please enter a 10-digit mobile number.');
        $('#mobile-input').css('border-color', 'red'); 
        $('#error-message').text('Invalid mobile number! Please enter a 10-digit mobile number.');
      }
    });
  });



//   video js
$(document).ready(function () {
    // get video source from data-src button
    var $videoSrc;
    $('.video-btn').click(function () {
      $videoSrc = $(this).data("src");
    });
    console.log($videoSrc);
    // autoplay video on modal load  
    $('#myModal').on('shown.bs.modal', function (e) {
      // youtube iframe configuration and settings
      $("#video").attr('src', $videoSrc + "?autoplay=1&rel=0&controls=1&loop=1&modestbranding=1");
    })
    // stop playing the youtube video when modal closed
    $('#myModal').on('hide.bs.modal', function (e) {
      // stop video
      $("#video").attr('src', $videoSrc);
    })
  });


// accordian
init__accordion();

      // Accordion
      function init__accordion() {
        // https://developer.mozilla.org/en-US/docs/Web/API/Element/animate
        // https://developer.mozilla.org/en-US/docs/Web/API/KeyframeEffect/KeyframeEffect#parameters
        let accordionItems = document.querySelectorAll('.accordion-tab');
        if (accordionItems.length > 0) {
          const speed = 250;
          const animationOptions = { duration: speed, iterations: 1, fill: "forwards" };

          // Handle Accordion On Init
          let init_true = document.querySelector('.accordion-tab[aria-selected="true"]');
          if (init_true) {
            let init_content = init_true.querySelector('.content');
            let init_content_parent = init_content.closest('.accordion-content');
            let init_content_height = init_content.clientHeight + 'px';

            let openKeyframes = [{ height: init_content_height }];
            init_content_parent.animate(openKeyframes, animationOptions);
          }

          // Handle Accordion On Click
          accordionItems.forEach(item => {
            item.addEventListener('click', e => {


              // Check if target is content. If content then exit.
              let tab_content = e.target.classList.contains('accordion-content');

              if (tab_content) { return false; }

              // Previous Active
              let prev_tab = document.querySelector('.accordion-tab[aria-selected="true"]');
              let prev_tab_content = null;
              prev_tab ? prev_tab_content = prev_tab.querySelector('.accordion-content') : null;

              // Current Active
              let curr_tab = e.target.closest('.accordion-tab');
              let curr_content = curr_tab.querySelector('.content');
              let curr_content_parent = curr_content.closest('.accordion-content');
              let curr_content_height = curr_content.clientHeight + 'px';

              // Animation
              let openKeyframes = [{ height: curr_content_height }];
              let closeKeyframes = [{ height: '0px' }];

              // Checking if this tab is already active
              let alreadyActive = curr_tab.getAttribute('aria-selected');

              // If there is an active tab, then close it
              prev_tab ? prev_tab_content.animate(closeKeyframes, animationOptions) : null;

              // Change Current Active
              if (alreadyActive == 'true') {
                // Close Current Tab
                curr_tab.setAttribute('aria-selected', false);
              } else {
                // Close Previous Open
                prev_tab ? prev_tab.setAttribute('aria-selected', false) : null;

                // Open Current Tab
                curr_tab.setAttribute('aria-selected', true);
                curr_content_parent.animate(openKeyframes, animationOptions);
              }
            });
          });
        }
      }



