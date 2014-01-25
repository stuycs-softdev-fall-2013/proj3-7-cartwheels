$(function () {
    "use strict";

    var $gallery = $('#gallery-cart');

    imagesLoaded($gallery, function () {
        resizeImages($gallery.get(0), 200);

        $gallery.cycle({
            fx: 'scrollRight',
            next: '#gallery-cart',
            timeout: 0
        });

        $gallery.find('img').css({'display': 'block'});
    });

    $.each(['name', 'owner', 'address'], function (index, item) {
        var el = $('.' + item);
        el.text(toTitleCase(el.text()));
    });
});
