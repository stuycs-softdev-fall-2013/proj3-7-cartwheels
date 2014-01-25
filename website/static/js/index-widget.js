$(function () {
    "use strict";

    var $gallery = $('#gallery'),
        $flag = $('#flag'),
        $inputBox = $('#search-input'),
        $inputText = $inputBox.find('input'),
        $mainContent = $('.main-content');

    $mainContent.removeClass('middle-bar');

    //when the images load, create collage
    var onImageLoad = function () {
        $(window).scrollTop(0);

        $gallery.removeWhitespace().collagePlus(
            {
                'targetHeight': 250,
                'fadeSpeed': 'fast',
                'effect': 'effect-2',
                'allowPartialLastRow': false
            }
        );
        $gallery.css({
            'opacity': 0.5
        }, 250);

        $flag.removeClass('hidden');
        $('body').css({'overflow': 'hidden'});
    };

    //initialize $gallery once all images load
    imagesLoaded($gallery.get(0), onImageLoad);

    //when user focuses on the input box
    var onInputFocus = function () {
        $flag.fadeOut(300);
        $('body').css({'overflow': 'scroll'});
        $gallery.animate({'opacity': 0.9});
    };

    $inputText.focus(onInputFocus);
});
