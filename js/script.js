$(window).scroll(function() {
    if($(this).scrollTop() < 100) {
        $('.navbar-fixed-top').addClass('opaque');
        $('.navbar-fixed-top').style.height = "50%";
    } else {
        $('.navbar-fixed-top').removeClass('opaque');
        $('.navbar-fixed-top').style.height = "100%";
    }
});