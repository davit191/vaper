$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        items: 4,
        nav: false,
        dots: false,
        autoplay: true,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        smartSpeed: 500,
        loop: true,
        
        margin: 17,
        responsive:{
            0:{
                items: 1,
                center: true
            },
            380:{
                items: 1,
            }, 
            480:{
                items: 2,
            },
            768:{
                items: 3,
                
            },
            1000:{
                items: 4
            }
        }
    });
});