$(document).ready(function () {
    $(".add-to-cart, .remove-from-cart").on("click", function () {
      $(this).parents(".flipable").toggleClass("flipped product-added");
      if ($(".product-added").length > 0) {
        $("body").addClass("enable-checkout");
      } else {
        $("body").removeClass("enable-checkout");
      }
    });
    $(".btn-checkout").on("click", function () {
      $("body").toggleClass("open-checkout");
    });
  
    var card = new Card({
      // a selector or DOM element for the form where users will
      // be entering their information
      form: ".form-container.active", // *required*
      // a selector or DOM element for the container
      // where you want the card to appear
      container: ".card-wrapper", // *required*
  
      //width: 200, // optional — default 350px
      formatting: true, // optional - default true
  
      // Strings for translation - optional
      messages: {
        validDate: "valid\ndate", // optional - default 'valid\nthru'
        monthYear: "mm/yyyy" // optional - default 'month/year'
      },
  
      // Default placeholders for rendered fields - optional
      placeholders: {
        number: "•••• •••• •••• ••••",
        name: "Full Name",
        expiry: "••/••",
        cvc: "•••"
      },
  
      // if true, will log helpful messages for setting up Card
      debug: true // optional - default false
    });
  });
  
  function demo() {
    setTimeout(function () {
      $(".add-to-cart:eq(0)").click();
      setTimeout(function () {
        $(".add-to-cart:eq(1)").click();
        setTimeout(function () {
          $(".btn-checkout").click();
        }, 500);
      }, 500);
    }, 1500);
  }
  