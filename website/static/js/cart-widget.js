$(function () {
    "use strict";

    var $gallery = $('#gallery-cart');

    //When all the images have loaded, create the gallery
    imagesLoaded($gallery, function () {

        //Resize the images before making the gallery
        resizeImages($gallery.get(0), 200);

        $gallery.cycle({
            fx: 'scrollRight',
            next: '#gallery-cart',
            timeout: 0
        });

        //Display the images (they are hidden before)
        $gallery.find('img').css({'display': 'block'});
    });

    //For each of these fields, maket the text title case
    $.each(['name', 'owner', 'address'], function (index, item) {
        var el = $('.' + item);
        el.text(toTitleCase(el.text()));
    });
});
