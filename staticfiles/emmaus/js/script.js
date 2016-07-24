$(".nav a").on("click", function(){
   $(".nav").find(".active").removeClass("active");
   $(this).parent().addClass("active");
});

function switch15() {
    var $dr16 = $('#dr16');
    var $dr15 = $('#dr15');

    jQuery($dr16).fadeOut(800);
    jQuery($dr15).fadeIn(800);
    
    $('#button16').removeClass("current");
    $('#button15').addClass("current");
}

function switch16() {
    var $dr16 = $('#dr16');
    var $dr15 = $('#dr15');

    jQuery($dr15).fadeOut(800);
	jQuery($dr16).fadeIn(800);
    
    $('#button16').addClass("current");
    $('#button15').removeClass("current");
}

$(".pop").on("click", function(e) {
    e.preventDefault();
   $('#imagepreview').attr('src', $(this).children('img').attr('src')); // here asign the image to the modal when the user click the enlarge link
   $('#imagemodal').modal('show'); // imagemodal is the id attribute assigned to the bootstrap modal, then i use the show function
});