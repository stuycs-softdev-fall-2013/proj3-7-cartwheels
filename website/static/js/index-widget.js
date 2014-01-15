$(function () {
    "use strict";

    //elements
    var gallery = $('#gallery'),
        flag = $('#flag'),
        inputBox = $('#search-input'),
        inputText = inputBox.find('input'),
        searchResults = $('#search-results'),
        header = $('#header');

    //other variables
    var targetImgHeight = 75;

    //when the images load, create collage
    var onImageLoad = function () {
        gallery.removeWhitespace().collagePlus(
            {
                'targetHeight': 250,
                'fadeSpeed': 'fast',
                'effect': 'effect-2',
                'allowPartialLastRow': false
            }
        );
        gallery.css({
            'opacity': 0.5
        }, 250);

        flag.removeClass('hidden');

        $('body').css({'overflow': 'hidden'});
    };

    //initialize gallery once all images load
    imagesLoaded(gallery.get(0), onImageLoad);

    //function to change image size based on aspect ratio in results
    var resizeImageResults = function () {
        var imageList = searchResults.find('img');

        imageList.each(function () {
            var $img = $(this);
            var w = (typeof $img.data("width") != 'undefined') ? $img.data("width") : $img.width(),
                h = (typeof $img.data("height") != 'undefined') ? $img.data("height") : $img.height(),
                aspectRatio = w / h,
                nw = aspectRatio * targetImgHeight;

            this.style.height = targetImgHeight + 'px';
            this.style.width = nw + 'px';
        });
    };

    //function to add border on bottom of last element
    var borderLast = function () {
        var searchItems = searchResults.find('.search-item'),
            lastItem = $(searchItems[searchItems.length - 1]);

        lastItem.css({
            'border-bottom': '1px solid #efefef'
        });
    };

    var onInputFocus = function () {
        flag.fadeOut(300);
        gallery.animate({'opacity': 0.9});
    };

    //when enter is pressed in the input box.  TODO: add ajax request
    var onInputSubmit = function (e) {
        if (e.keyCode === 13) {
            gallery.fadeOut(500, function () {
                $('#search-results').css({
                    'display': 'block'
                });

                $('body').css({'overflow': 'scroll'});
            });

            //Creating and styling the results list
            resizeImageResults();
            borderLast();
        }
    };

    //when enter is pressed
    inputText.focus(onInputFocus);
    inputText.on('keypress', onInputSubmit);

    var positionHeader = function () {
        var $window = $(window);
        var headerTop = $window.scrollTop();

        header.css({
            'top': headerTop
        });
    };

    positionHeader();
    $(window).scroll(positionHeader);
});
