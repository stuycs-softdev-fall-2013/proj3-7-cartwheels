$(function () {
    "use strict";

    //elements
    var $header = $('#header');

    //keep header on the top of the page
    var positionHeader = function () {
        var $window = $(window);
        var $headerTop = $window.scrollTop();

        $header.css({
            'top': $headerTop
        });
    };

    positionHeader();
    $(window).scroll(positionHeader);
});
