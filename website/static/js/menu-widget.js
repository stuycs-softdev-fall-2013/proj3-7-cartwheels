$(function () {
    "use strict";

    var $mainContent = $('.main-content'),
        $menu = $('#menu');

    imagesLoaded($menu, function () {
        resizeImages($menu.get(0), 75);
    });
});
